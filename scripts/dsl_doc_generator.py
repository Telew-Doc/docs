#!/usr/bin/env python3
"""
DSL Documentation Generator

This script parses all DSL (.erp) files from the dsl-apps repository and generates
comprehensive technical documentation including:
- API reference with all methods, fields, and properties
- Inheritance hierarchies
- Cross-references between related types
- Dependency mapping between apps
- Generated entities and their relationships

Usage:
    python scripts/dsl_doc_generator.py

Output:
    - docs/generated/api/ - Technical API documentation
    - docs/generated/dependencies/ - App dependency documentation
    - docs/generated/inheritance/ - Type hierarchy documentation
"""

import os
import re
import json
import sys
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any
from dataclasses import dataclass, field
from collections import defaultdict
import argparse

@dataclass
class DSLField:
    """Represents a field in a DSL entity"""
    name: str
    type: str
    modifiers: List[str] = field(default_factory=list)
    default_value: Optional[str] = None
    description: Optional[str] = None
    is_ref: bool = False
    is_system: bool = False
    is_const: bool = False
    is_computed: bool = False

@dataclass
class DSLFunction:
    """Represents a function in a DSL entity"""
    name: str
    return_type: Optional[str] = None
    parameters: List[Tuple[str, str]] = field(default_factory=list)
    modifiers: List[str] = field(default_factory=list)
    body: Optional[str] = None
    is_native: bool = False
    is_abstract: bool = False
    is_override: bool = False
    is_impl: bool = False

@dataclass
class DSLView:
    """Represents a view in a DSL entity"""
    name: str
    body: Optional[str] = None
    modifiers: List[str] = field(default_factory=list)

@dataclass
class DSLEvent:
    """Represents an event in a DSL entity"""
    name: str
    event_type: str  # 'front' or 'back'
    return_type: Optional[str] = None
    body: Optional[str] = None

@dataclass
class DSLEntity:
    """Represents a DSL entity (trait, entity, interface, enum, etc.)"""
    name: str
    type: str  # trait, entity, interface, enum, object, etc.
    app_name: str
    file_path: str
    extends: List[str] = field(default_factory=list)
    implements: List[str] = field(default_factory=list)
    fields: List[DSLField] = field(default_factory=list)
    functions: List[DSLFunction] = field(default_factory=list)
    views: List[DSLView] = field(default_factory=list)
    events: List[DSLEvent] = field(default_factory=list)
    modifiers: List[str] = field(default_factory=list)
    description: Optional[str] = None
    enum_cases: List[str] = field(default_factory=list)
    generator_params: Dict[str, Any] = field(default_factory=dict)

@dataclass
class DSLApp:
    """Represents a DSL application"""
    name: str
    version: str
    path: str
    dependencies: List[str] = field(default_factory=list)
    entities: List[DSLEntity] = field(default_factory=list)
    uuid: Optional[str] = None
    status: Optional[str] = None

class DSLParser:
    """Parser for DSL files"""
    
    def __init__(self, dsl_apps_path: str):
        self.dsl_apps_path = Path(dsl_apps_path)
        self.erp_path = self.dsl_apps_path / "src" / "main" / "erp"
        self.apps: Dict[str, DSLApp] = {}
        self.all_entities: Dict[str, DSLEntity] = {}
        
    def parse_all_apps(self) -> Dict[str, DSLApp]:
        """Parse all DSL applications"""
        print("Scanning for DSL applications...")
        
        if not self.erp_path.exists():
            raise FileNotFoundError(f"ERP path not found: {self.erp_path}")
            
        for app_dir in self.erp_path.iterdir():
            if app_dir.is_dir():
                try:
                    app = self._parse_app(app_dir)
                    if app:
                        self.apps[app.name] = app
                        print(f"Parsed app: {app.name} (v{app.version}) - {len(app.entities)} entities")
                except Exception as e:
                    print(f"Error parsing app {app_dir.name}: {e}")
                    
        print(f"Total apps parsed: {len(self.apps)}")
        print(f"Total entities: {sum(len(app.entities) for app in self.apps.values())}")
        
        # Build global entity index
        for app in self.apps.values():
            for entity in app.entities:
                full_name = f"{app.name}.{entity.name}"
                self.all_entities[full_name] = entity
                self.all_entities[entity.name] = entity  # Also index by short name
                
        return self.apps
    
    def _parse_app(self, app_dir: Path) -> Optional[DSLApp]:
        """Parse a single DSL application"""
        # Find the version directory (should be only one)
        version_dirs = [d for d in app_dir.iterdir() if d.is_dir()]
        if not version_dirs:
            return None
            
        version_dir = version_dirs[0]  # Take the first (and usually only) version
        version = version_dir.name
        
        # Parse AppSource.properties if it exists
        app_source_file = version_dir / "AppSource.properties"
        dependencies = []
        uuid = None
        status = None
        
        if app_source_file.exists():
            deps, uuid, status = self._parse_app_source(app_source_file)
            dependencies = deps
            
        app = DSLApp(
            name=app_dir.name,
            version=version,
            path=str(version_dir),
            dependencies=dependencies,
            uuid=uuid,
            status=status
        )
        
        # Parse all .erp files in the version directory
        for erp_file in version_dir.glob("*.erp"):
            try:
                entities = self._parse_erp_file(erp_file, app.name)
                app.entities.extend(entities)
            except Exception as e:
                print(f"Error parsing {erp_file}: {e}")
                
        return app
    
    def _parse_app_source(self, app_source_file: Path) -> Tuple[List[str], Optional[str], Optional[str]]:
        """Parse AppSource.properties file"""
        dependencies = []
        uuid = None
        status = None
        
        try:
            with open(app_source_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse dependencies
            deps_match = re.search(r'dependencies\s*=\s*\[(.*?)\]', content, re.DOTALL)
            if deps_match:
                deps_str = deps_match.group(1)
                # Extract dslPackage values
                for match in re.finditer(r'dslPackage\s*:\s*([^,}]+)', deps_str):
                    dep_name = match.group(1).strip()
                    dependencies.append(dep_name)
                    
            # Parse UUID
            uuid_match = re.search(r'uuid\s*=\s*(\d+)', content)
            if uuid_match:
                uuid = uuid_match.group(1)
                
            # Parse status
            status_match = re.search(r'status\s*=\s*(\w+)', content)
            if status_match:
                status = status_match.group(1)
                
        except Exception as e:
            print(f"Error parsing {app_source_file}: {e}")
            
        return dependencies, uuid, status
    
    def _parse_erp_file(self, erp_file: Path, app_name: str) -> List[DSLEntity]:
        """Parse a single .erp file"""
        with open(erp_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        entities = []
        
        # Split content into top-level declarations
        declarations = self._split_declarations(content)
        
        for decl in declarations:
            entity = self._parse_declaration(decl, app_name, str(erp_file))
            if entity:
                entities.append(entity)
                
        return entities
    
    def _split_declarations(self, content: str) -> List[str]:
        """Split content into top-level declarations"""
        # This is a simplified approach - in reality, we'd need a proper parser
        # for handling nested braces correctly
        declarations = []
        current_decl = ""
        brace_count = 0
        in_string = False
        escape_next = False
        
        lines = content.split('\n')
        
        for line in lines:
            stripped = line.strip()
            
            # Skip comments and empty lines at the top level
            if not current_decl and (not stripped or stripped.startswith('//')):
                continue
                
            current_decl += line + '\n'
            
            # Count braces (simplified - doesn't handle strings properly)
            for char in line:
                if escape_next:
                    escape_next = False
                    continue
                    
                if char == '\\':
                    escape_next = True
                    continue
                    
                if char == '"' and not escape_next:
                    in_string = not in_string
                    continue
                    
                if not in_string:
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        
            # If we've closed all braces and have content, we have a complete declaration
            if brace_count == 0 and current_decl.strip():
                # Check if this looks like a declaration
                if self._is_declaration(current_decl):
                    declarations.append(current_decl.strip())
                current_decl = ""
                
        # Add any remaining content
        if current_decl.strip():
            declarations.append(current_decl.strip())
            
        return declarations
    
    def _is_declaration(self, content: str) -> bool:
        """Check if content looks like a DSL declaration"""
        first_line = content.strip().split('\n')[0].strip()
        
        # Check for DSL keywords
        keywords = [
            'trait', 'entity', 'interface', 'enum', 'object', 'class',
            'extend', 'generator', 'acctemplate', 'account', 'analytic',
            'report', 'register', 'inline'
        ]
        
        for keyword in keywords:
            if first_line.startswith(keyword + ' '):
                return True
                
        return False
    
    def _parse_declaration(self, content: str, app_name: str, file_path: str) -> Optional[DSLEntity]:
        """Parse a single DSL declaration"""
        lines = content.strip().split('\n')
        if not lines:
            return None
            
        first_line = lines[0].strip()
        
        # Parse the declaration header
        entity_info = self._parse_declaration_header(first_line)
        if not entity_info:
            return None
            
        entity_type, entity_name, extends, implements, modifiers = entity_info
        
        entity = DSLEntity(
            name=entity_name,
            type=entity_type,
            app_name=app_name,
            file_path=file_path,
            extends=extends,
            implements=implements,
            modifiers=modifiers
        )
        
        # Parse the body
        body_content = '\n'.join(lines[1:]) if len(lines) > 1 else ""
        self._parse_entity_body(entity, body_content)
        
        return entity
    
    def _parse_declaration_header(self, header: str) -> Optional[Tuple[str, str, List[str], List[str], List[str]]]:
        """Parse declaration header line"""
        # Remove opening brace if present
        header = header.rstrip(' {')
        
        # Handle different declaration types
        patterns = [
            # trait Name extends Parent with Interface
            r'(trait|entity|interface|class|object|register|report)\s+(\w+)(?:\s+extends\s+([\w\s,]+?))?(?:\s+with\s+([\w\s,]+?))?$',
            # enum Name
            r'(enum)\s+(\w+)(?:\([^)]*\))?$',
            # generator name
            r'(generator)\s+(\w+)$',
            # acctemplate Name
            r'(acctemplate)\s+(\w+)(?:\([^)]*\))?$',
            # account Name
            r'(account)\s+(\w+)$',
            # analytic Name
            r'(analytic)\s+(\w+)(?:\([^)]*\))?$',
            # extend trait/entity Name
            r'extend\s+(trait|entity|interface|class|object|register|report)\s+(\w+)$',
            # inline trait/entity Name
            r'(inline)\s+(trait|entity|interface|class)\s+(\w+)(?:\s+extends\s+([\w\s,]+?))?(?:\s+with\s+([\w\s,]+?))?$',
        ]
        
        for pattern in patterns:
            match = re.match(pattern, header, re.IGNORECASE)
            if match:
                groups = match.groups()
                
                if header.startswith('extend'):
                    entity_type = f"extend {groups[0]}"
                    entity_name = groups[1]
                    extends = []
                    implements = []
                    modifiers = ['extend']
                elif header.startswith('inline'):
                    entity_type = groups[1]
                    entity_name = groups[2]
                    extends = self._parse_type_list(groups[3]) if len(groups) > 3 and groups[3] else []
                    implements = self._parse_type_list(groups[4]) if len(groups) > 4 and groups[4] else []
                    modifiers = ['inline']
                else:
                    entity_type = groups[0]
                    entity_name = groups[1]
                    extends = self._parse_type_list(groups[2]) if len(groups) > 2 and groups[2] else []
                    implements = self._parse_type_list(groups[3]) if len(groups) > 3 and groups[3] else []
                    modifiers = []
                
                return entity_type, entity_name, extends, implements, modifiers
                
        return None
    
    def _parse_type_list(self, type_str: str) -> List[str]:
        """Parse a comma-separated list of types"""
        if not type_str:
            return []
        return [t.strip() for t in type_str.split(',') if t.strip()]
    
    def _parse_entity_body(self, entity: DSLEntity, body: str):
        """Parse the body of an entity declaration"""
        if not body.strip():
            return
            
        # Split body into members (fields, functions, views, etc.)
        members = self._split_members(body)
        
        for member in members:
            self._parse_member(entity, member)
    
    def _split_members(self, body: str) -> List[str]:
        """Split entity body into individual members"""
        if not body.strip():
            return []
            
        members = []
        lines = body.split('\n')
        current_member = ""
        brace_count = 0
        in_string = False
        paren_count = 0
        bracket_count = 0
        
        i = 0
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            
            # Skip empty lines and comments at the top level when not in a member
            if not current_member and (not stripped or stripped.startswith('//')):
                i += 1
                continue
            
            # Check if this line starts a new member
            if not current_member and self._is_member_start(stripped):
                current_member = line + '\n'
                brace_count = 0
                in_string = False
                paren_count = 0
                bracket_count = 0
                
                # Count braces/parens/brackets in this line
                for char in line:
                    if char == '"' and (len(line) == 0 or line[line.index(char)-1] != '\\'):
                        in_string = not in_string
                    elif not in_string:
                        if char == '{':
                            brace_count += 1
                        elif char == '}':
                            brace_count -= 1
                        elif char == '(':
                            paren_count += 1
                        elif char == ')':
                            paren_count -= 1
                        elif char == '[':
                            bracket_count += 1
                        elif char == ']':
                            bracket_count -= 1
                
                # Check if this is a simple one-liner (no opening brace or ends with simple assignment)
                if (brace_count == 0 and paren_count == 0 and bracket_count == 0 and 
                    (not '{' in line or line.rstrip().endswith('}'))):
                    members.append(current_member.strip())
                    current_member = ""
                
                i += 1
                continue
            
            # If we're in a member, add this line
            if current_member:
                current_member += line + '\n'
                
                # Count braces/parens/brackets in this line
                for char in line:
                    if char == '"' and (len(line) == 0 or line[line.index(char)-1] != '\\'):
                        in_string = not in_string
                    elif not in_string:
                        if char == '{':
                            brace_count += 1
                        elif char == '}':
                            brace_count -= 1
                        elif char == '(':
                            paren_count += 1
                        elif char == ')':
                            paren_count -= 1
                        elif char == '[':
                            bracket_count += 1
                        elif char == ']':
                            bracket_count -= 1
                
                # If all braces/parens/brackets are closed, we have a complete member
                if brace_count <= 0 and paren_count <= 0 and bracket_count <= 0:
                    members.append(current_member.strip())
                    current_member = ""
                    brace_count = 0
                    paren_count = 0
                    bracket_count = 0
            
            i += 1
        
        # Add any remaining content
        if current_member.strip():
            members.append(current_member.strip())
            
        return members
    
    def _is_member_start(self, line: str) -> bool:
        """Check if line starts a new member"""
        if not line:
            return False
            
        # Member start patterns
        patterns = [
            r'^(field|ref\s+field|system\s+field|const\s+field)\s+\w+',
            r'^(compute)\s+\w+',
            r'^(func|native|impl\s+func|override\s+func|back\s+func|front\s+func)\s+\w+',
            r'^(view|impl\s+view|override\s+view)\s+\w+',
            r'^(front\s+event|back\s+event|event)\s+\w+',
            r'^case\s+\w+',
            r'^(object\s+)?(field|func|view)\s+\w+',
            r'^(report|class|trait|entity|interface|enum|object)\s+\w+',
        ]
        
        for pattern in patterns:
            if re.match(pattern, line):
                return True
                
        return False
    
    def _is_complete_member(self, content: str) -> bool:
        """Check if content represents a complete member"""
        stripped = content.strip()
        if not stripped:
            return False
            
        # Check for member patterns
        first_line = stripped.split('\n')[0].strip()
        
        # Field patterns
        if re.match(r'(field|ref\s+field|system\s+field|const\s+field|compute)', first_line):
            return True
            
        # Function patterns
        if re.match(r'(func|native|impl\s+func|override\s+func)', first_line):
            return True
            
        # View patterns
        if re.match(r'(view|impl\s+view|override\s+view)', first_line):
            return True
            
        # Event patterns
        if re.match(r'(front\s+event|back\s+event|event)', first_line):
            return True
            
        # Enum case
        if re.match(r'case\s+\w+', first_line):
            return True
            
        return False
    
    def _parse_member(self, entity: DSLEntity, member: str):
        """Parse a single member (field, function, view, etc.)"""
        lines = member.strip().split('\n')
        if not lines:
            return
            
        first_line = lines[0].strip()
        
        # Parse different member types
        if self._is_field(first_line):
            field = self._parse_field(member)
            if field:
                entity.fields.append(field)
        elif self._is_function(first_line):
            function = self._parse_function(member)
            if function:
                entity.functions.append(function)
        elif self._is_view(first_line):
            view = self._parse_view(member)
            if view:
                entity.views.append(view)
        elif self._is_event(first_line):
            event = self._parse_event(member)
            if event:
                entity.events.append(event)
        elif self._is_enum_case(first_line):
            case_name = self._parse_enum_case(first_line)
            if case_name:
                entity.enum_cases.append(case_name)
    
    def _is_field(self, line: str) -> bool:
        """Check if line starts a field declaration"""
        patterns = [
            r'^(field|ref\s+field|system\s+field|const\s+field)\s+\w+',
            r'^(compute)\s+\w+',
            r'^(system\s+compute|const\s+system\s+field)\s+\w+',
        ]
        
        for pattern in patterns:
            if re.match(pattern, line):
                return True
        return False
    
    def _is_function(self, line: str) -> bool:
        """Check if line starts a function declaration"""
        patterns = [
            r'^(func|native)\s+\w+',
            r'^(impl\s+func|override\s+func)\s+\w+',
            r'^(back\s+func|front\s+func)\s+\w+',
            r'^(back\s+native|front\s+native)\s+\w+',
            r'^(impl\s+final\s+func|override\s+final\s+func)\s+\w+',
            r'^(object\s+func|object\s+native)\s+\w+',
            r'^(back\s+object\s+func)\s+\w+',
        ]
        
        for pattern in patterns:
            if re.match(pattern, line):
                return True
        return False
    
    def _is_view(self, line: str) -> bool:
        """Check if line starts a view declaration"""
        return bool(re.match(r'(view|impl\s+view|override\s+view)', line))
    
    def _is_event(self, line: str) -> bool:
        """Check if line starts an event declaration"""
        return bool(re.match(r'(front\s+event|back\s+event|event)', line))
    
    def _is_enum_case(self, line: str) -> bool:
        """Check if line is an enum case"""
        return bool(re.match(r'case\s+\w+', line))
    
    def _parse_field(self, content: str) -> Optional[DSLField]:
        """Parse a field declaration"""
        lines = content.strip().split('\n')
        if not lines:
            return None
            
        first_line = lines[0].strip()
        
        # Extract modifiers and field info
        modifiers = []
        is_ref = 'ref' in first_line
        is_system = 'system' in first_line
        is_const = 'const' in first_line
        is_computed = first_line.strip().startswith('compute')
        
        if is_ref:
            modifiers.append('ref')
        if is_system:
            modifiers.append('system')
        if is_const:
            modifiers.append('const')
        if is_computed:
            modifiers.append('compute')
            
        # Parse field name and type - handle various patterns
        patterns = [
            # field name: Type = value
            r'(?:field|compute)\s+(\w+)\s*:\s*([^=\{]+?)(?:\s*=|\s*\{|$)',
            # field name = value (inferred type)
            r'(?:field|compute)\s+(\w+)(?:\s*=|\s*\{)',
            # field name { ... } (complex field)
            r'(?:field|compute)\s+(\w+)\s*\{',
        ]
        
        name = None
        field_type = None
        
        for pattern in patterns:
            match = re.search(pattern, first_line)
            if match:
                name = match.group(1)
                if len(match.groups()) > 1:
                    field_type = match.group(2).strip() if match.group(2) else None
                break
        
        if name:
            # Extract default value if present
            default_value = None
            if '=' in first_line and not '{' in first_line:
                parts = first_line.split('=', 1)
                if len(parts) > 1:
                    default_value = parts[1].strip()
            
            return DSLField(
                name=name,
                type=field_type or "Unknown",
                modifiers=modifiers,
                default_value=default_value,
                is_ref=is_ref,
                is_system=is_system,
                is_const=is_const,
                is_computed=is_computed
            )
            
        return None
    
    def _parse_function(self, content: str) -> Optional[DSLFunction]:
        """Parse a function declaration"""
        lines = content.strip().split('\n')
        if not lines:
            return None
            
        first_line = lines[0].strip()
        
        modifiers = []
        is_native = 'native' in first_line
        is_impl = first_line.strip().startswith('impl')
        is_override = 'override' in first_line
        is_back = 'back' in first_line
        is_front = 'front' in first_line
        is_object = 'object' in first_line
        
        if is_native:
            modifiers.append('native')
        if is_impl:
            modifiers.append('impl')
        if is_override:
            modifiers.append('override')
        if is_back:
            modifiers.append('back')
        if is_front:
            modifiers.append('front')
        if is_object:
            modifiers.append('object')
            
        # Parse function signature - handle various patterns
        patterns = [
            # func name(params): ReturnType = body
            r'func\s+(\w+)\s*\(([^)]*)\)\s*:\s*([^=\{]+?)(?:\s*=|\s*\{|$)',
            # func name(params) = body (inferred return type)
            r'func\s+(\w+)\s*\(([^)]*)\)(?:\s*=|\s*\{|$)',
            # func name: ReturnType = body (no params)
            r'func\s+(\w+)\s*:\s*([^=\{]+?)(?:\s*=|\s*\{|$)',
            # func name = body (no params, inferred return type)
            r'func\s+(\w+)(?:\s*=|\s*\{|$)',
            # native name(params): ReturnType
            r'native\s+(\w+)\s*\(([^)]*)\)\s*:\s*([^=\{]+?)(?:\s*=|\s*\{|$)',
            # native name: ReturnType
            r'native\s+(\w+)\s*:\s*([^=\{]+?)(?:\s*=|\s*\{|$)',
            # native name
            r'native\s+(\w+)(?:\s*=|\s*\{|$)',
        ]
        
        name = None
        return_type = None
        parameters = []
        
        for pattern in patterns:
            match = re.search(pattern, first_line)
            if match:
                groups = match.groups()
                name = groups[0]
                
                # Determine which group is params and which is return type
                if len(groups) >= 3:  # name, params, return_type
                    params_str = groups[1] if groups[1] else ""
                    return_type = groups[2].strip() if groups[2] else None
                elif len(groups) == 2:
                    # Could be (name, params) or (name, return_type)
                    if '(' in first_line and ')' in first_line:
                        params_str = groups[1] if groups[1] else ""
                    else:
                        return_type = groups[1].strip() if groups[1] else None
                        params_str = ""
                else:
                    params_str = ""
                
                # Parse parameters if present
                if 'params_str' in locals() and params_str:
                    # Simple parameter parsing - could be improved
                    param_parts = [p.strip() for p in params_str.split(',') if p.strip()]
                    for param in param_parts:
                        if ':' in param:
                            param_name, param_type = param.split(':', 1)
                            parameters.append((param_name.strip(), param_type.strip()))
                        else:
                            parameters.append((param.strip(), "Unknown"))
                
                break
        
        if name:
            return DSLFunction(
                name=name,
                return_type=return_type,
                parameters=parameters,
                modifiers=modifiers,
                is_native=is_native,
                is_impl=is_impl,
                is_override=is_override
            )
            
        return None
    
    def _parse_view(self, content: str) -> Optional[DSLView]:
        """Parse a view declaration"""
        first_line = content.strip().split('\n')[0]
        
        modifiers = []
        if first_line.strip().startswith('impl'):
            modifiers.append('impl')
        if 'override' in first_line:
            modifiers.append('override')
            
        match = re.search(r'view\s+(\w+)', first_line)
        if match:
            name = match.group(1)
            return DSLView(name=name, modifiers=modifiers)
            
        return None
    
    def _parse_event(self, content: str) -> Optional[DSLEvent]:
        """Parse an event declaration"""
        first_line = content.strip().split('\n')[0]
        
        event_type = 'back'  # default
        if first_line.strip().startswith('front'):
            event_type = 'front'
            
        match = re.search(r'event\s+(\w+)(?:\s*:\s*([^=\{]+?))?', first_line)
        if match:
            name = match.group(1)
            return_type = match.group(2).strip() if match.group(2) else None
            
            return DSLEvent(
                name=name,
                event_type=event_type,
                return_type=return_type
            )
            
        return None
    
    def _parse_enum_case(self, line: str) -> Optional[str]:
        """Parse an enum case"""
        match = re.search(r'case\s+(\w+)', line)
        if match:
            return match.group(1)
        return None

class DocumentationGenerator:
    """Generates documentation from parsed DSL data"""
    
    def __init__(self, apps: Dict[str, DSLApp], output_dir: str):
        self.apps = apps
        self.output_dir = Path(output_dir)
        self.all_entities = {}
        
        # Build entity index
        for app in apps.values():
            for entity in app.entities:
                full_name = f"{app.name}.{entity.name}"
                self.all_entities[full_name] = entity
                self.all_entities[entity.name] = entity
    
    def generate_all_docs(self):
        """Generate all documentation"""
        print("Generating documentation...")
        
        # Create output directories
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "apps").mkdir(exist_ok=True)
        
        # Generate different types of documentation
        self._generate_apps_docs()
        self._generate_dependency_docs()
        self._generate_inheritance_docs()
        self._generate_index()
        
        print(f"Documentation generated in: {self.output_dir}")
    
    def _generate_apps_docs(self):
        """Generate apps documentation"""
        print("Generating apps documentation...")
        
        apps_dir = self.output_dir / "apps"
        
        # Generate documentation for each app
        app_names = []
        for app_name, app in self.apps.items():
            app_dir_name = app_name.replace('.', '_')
            app_dir = apps_dir / app_dir_name
            app_dir.mkdir(exist_ok=True)
            app_names.append(app_dir_name)
            
            # Generate app overview
            self._generate_app_overview(app, app_dir)
            
            # Generate entity documentation and collect entity names
            entity_names = []
            for entity in app.entities:
                self._generate_entity_doc(entity, app_dir)
                entity_names.append(entity.name)
            
            # Generate .nav.yml for this app
            self._generate_app_nav(app_dir, entity_names)
        
        # Generate main apps .nav.yml
        self._generate_apps_nav(apps_dir, app_names)
    
    def _generate_app_overview(self, app: DSLApp, app_dir: Path):
        """Generate API overview for an app"""
        content = f"""# {app.name} API Reference

**Version:** {app.version}
**Status:** {app.status or 'Unknown'}

## Overview

This app contains {len(app.entities)} entities.

## Dependencies

"""
        
        if app.dependencies:
            for dep in app.dependencies:
                content += f"- `{dep}`\n"
        else:
            content += "No dependencies\n"
            
        content += "\n## Entities\n\n"
        
        # Group entities by type
        by_type = defaultdict(list)
        for entity in app.entities:
            by_type[entity.type].append(entity)
            
        for entity_type, entities in sorted(by_type.items()):
            content += f"### {entity_type.title()}s\n\n"
            for entity in sorted(entities, key=lambda e: e.name):
                content += f"- [`{entity.name}`](./{entity.name}.md)\n"
            content += "\n"
            
        with open(app_dir / "README.md", 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _generate_app_nav(self, app_dir: Path, entity_names: List[str]):
        """Generate .nav.yml for a single app"""
        nav_content = "nav:\n"
        nav_content += "  - README.md\n"
        
        # Add entities in alphabetical order
        for entity_name in sorted(entity_names):
            nav_content += f"  - {entity_name}.md\n"
        
        with open(app_dir / ".nav.yml", 'w', encoding='utf-8') as f:
            f.write(nav_content)
    
    def _generate_apps_nav(self, apps_dir: Path, app_names: List[str]):
        """Generate .nav.yml for the apps directory"""
        nav_content = "nav:\n"
        
        # Add apps in alphabetical order
        for app_name in sorted(app_names):
            nav_content += f"  - {app_name}\n"
        
        with open(apps_dir / ".nav.yml", 'w', encoding='utf-8') as f:
            f.write(nav_content)
    
    def _generate_entity_doc(self, entity: DSLEntity, app_dir: Path):
        """Generate documentation for a single entity"""
        content = f"""# {entity.name}

**Type:** {entity.type}  
**App:** {entity.app_name}

"""
        
        if entity.modifiers:
            content += f"**Modifiers:** {', '.join(entity.modifiers)}\n\n"
            
        if entity.extends:
            # Create links to the extended types
            extends_links = []
            for ext in entity.extends:
                # Try to find the app that contains this type
                ext_app = None
                for app_name, app in self.apps.items():
                    for ent in app.entities:
                        if ent.name == ext:
                            ext_app = app_name.replace('.', '_')
                            break
                    if ext_app:
                        break
                
                if ext_app:
                    extends_links.append(f"[`{ext}`](../{ext_app}/{ext}.md)")
                else:
                    extends_links.append(f"`{ext}`")
            
            content += "**Extends:** " + ", ".join(extends_links) + "\n\n"
            
        if entity.implements:
            content += "**Implements:** " + ", ".join(f"`{impl}`" for impl in entity.implements) + "\n\n"
            
        # Fields
        if entity.fields:
            content += "## Fields\n\n"
            for field in entity.fields:
                content += f"### `{field.name}`\n\n"
                content += f"**Type:** `{field.type}`\n\n"
                if field.modifiers:
                    content += f"**Modifiers:** {', '.join(field.modifiers)}\n\n"
                content += "---\n\n"
        
        # Functions
        if entity.functions:
            content += "## Functions\n\n"
            for func in entity.functions:
                content += f"### `{func.name}`\n\n"
                if func.return_type:
                    content += f"**Returns:** `{func.return_type}`\n\n"
                if func.modifiers:
                    content += f"**Modifiers:** {', '.join(func.modifiers)}\n\n"
                content += "---\n\n"
        
        # Views
        if entity.views:
            content += "## Views\n\n"
            for view in entity.views:
                content += f"### `{view.name}`\n\n"
                if view.modifiers:
                    content += f"**Modifiers:** {', '.join(view.modifiers)}\n\n"
                content += "---\n\n"
        
        # Events
        if entity.events:
            content += "## Events\n\n"
            for event in entity.events:
                content += f"### `{event.name}` ({event.event_type})\n\n"
                if event.return_type:
                    content += f"**Returns:** `{event.return_type}`\n\n"
                content += "---\n\n"
        
        # Enum cases
        if entity.enum_cases:
            content += "## Cases\n\n"
            for case in entity.enum_cases:
                content += f"- `{case}`\n"
            content += "\n"
            
        with open(app_dir / f"{entity.name}.md", 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _generate_dependency_docs(self):
        """Generate dependency documentation"""
        print("Generating dependency documentation...")
        
        # Generate dependency graph
        content = "# App Dependencies\n\n"
        content += "## Dependency Graph\n\n"
        content += "```mermaid\ngraph TD\n"
        
        for app_name, app in self.apps.items():
            safe_name = app_name.replace('.', '_').replace('-', '_')
            for dep in app.dependencies:
                safe_dep = dep.replace('.', '_').replace('-', '_')
                content += f"    {safe_name} --> {safe_dep}\n"
                
        content += "```\n\n"
        
        # Generate dependency table
        content += "## Dependency Details\n\n"
        content += "| App | Version | Dependencies |\n"
        content += "|-----|---------|-------------|\n"
        
        for app_name, app in sorted(self.apps.items()):
            deps_str = ", ".join(app.dependencies) if app.dependencies else "None"
            content += f"| `{app_name}` | {app.version} | {deps_str} |\n"
            
        with open(self.output_dir / "dependencies.md", 'w', encoding='utf-8') as f:
            f.write(content)
    
    def _generate_inheritance_docs(self):
        """Generate inheritance hierarchy documentation"""
        print("Generating inheritance documentation...")
        
        # Build inheritance tree
        inheritance_tree = defaultdict(list)
        all_types = set()
        
        for app in self.apps.values():
            for entity in app.entities:
                all_types.add(entity.name)
                for parent in entity.extends:
                    inheritance_tree[parent].append(entity.name)
                    all_types.add(parent)
        
        content = "# Type Inheritance Hierarchy\n\n"
        
        # Find root types (types that don't extend anything)
        root_types = []
        for app in self.apps.values():
            for entity in app.entities:
                if not entity.extends:
                    root_types.append(entity.name)
        
        content += "## Inheritance Tree\n\n"
        
        def write_tree(type_name: str, level: int = 0) -> str:
            indent = "  " * level
            result = f"{indent}- `{type_name}`\n"
            
            children = inheritance_tree.get(type_name, [])
            for child in sorted(children):
                result += write_tree(child, level + 1)
                
            return result
        
        for root in sorted(set(root_types)):
            if root in inheritance_tree:  # Only show roots that have children
                content += write_tree(root)
                content += "\n"
        
        with open(self.output_dir / "inheritance.md", 'w', encoding='utf-8') as f:
            f.write(content)
    

    
    def _generate_index(self):
        """Generate main index file"""
        content = """# DSL Documentation

This documentation is automatically generated from the DSL source code.

## Sections

- [Apps](apps/) - Complete API documentation for all apps and entities
- [Dependencies](dependencies.md) - App dependency relationships
- [Inheritance](inheritance.md) - Type inheritance hierarchies

## Quick Stats

"""
        
        total_apps = len(self.apps)
        total_entities = sum(len(app.entities) for app in self.apps.values())
        
        content += f"- **{total_apps}** applications\n"
        content += f"- **{total_entities}** entities\n"
        
        # Entity type breakdown
        type_counts = defaultdict(int)
        for app in self.apps.values():
            for entity in app.entities:
                type_counts[entity.type] += 1
                
        content += "\n### Entity Types\n\n"
        for entity_type, count in sorted(type_counts.items()):
            content += f"- **{count}** {entity_type}s\n"
            
        with open(self.output_dir / "index.md", 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Generate main .nav.yml
        nav_content = """nav:
  - index.md
  - apps
  - dependencies.md
  - inheritance.md
"""
        
        with open(self.output_dir / ".nav.yml", 'w', encoding='utf-8') as f:
            f.write(nav_content)

def main():
    parser = argparse.ArgumentParser(description='Generate DSL documentation')
    parser.add_argument('--dsl-path', default='dsl-apps', 
                       help='Path to DSL apps directory (default: dsl-apps)')
    parser.add_argument('--output', default='docs/generated',
                       help='Output directory (default: docs/generated)')
    
    args = parser.parse_args()
    
    try:
        # Parse DSL files
        dsl_parser = DSLParser(args.dsl_path)
        apps = dsl_parser.parse_all_apps()
        
        if not apps:
            print("No DSL applications found!")
            return 1
            
        # Generate documentation
        doc_generator = DocumentationGenerator(apps, args.output)
        doc_generator.generate_all_docs()
        
        print("Documentation generation completed successfully!")
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main()) 