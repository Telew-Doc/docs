# DSL Linker Documentation

## Overview

The DSL Linker is a crucial component of the ERP system that handles the linking and resolution of DSL (Domain Specific Language) code. It's responsible for:

- Resolving type references
- Linking declarations
- Handling class inheritance and extensions
- Managing environment availability (Back/Front)
- Processing properties and expressions

## Core Components

### 1. DslLinker

The main entry point for the linking process. Key responsibilities:

- Linking AST (Abstract Syntax Tree) with dependencies
- Managing class resolution
- Handling type linking
- Processing declarations

```scala
object DslLinker {
  def apply(ast: LinkAst, deps: List[Dependency])(implicit idGen: DslIdGen): Checked[LinkAst]
  def linkExpr(envAvailability: EnvAvailability, expr: Expr, deps: List[Dependency])(implicit idGen: DslIdGen): Checked[Expr]
  def linkGeneratorCall(envAvailability: EnvAvailability, expr: Expr, deps: List[Dependency], selfId: DslId)(implicit idGen: DslIdGen): Checked[Expr]
}
```

### 2. LinkAst

Represents the linked AST structure:

- Contains application components and statements
- Handles class uniqueness checks
- Manages environment availability
- Provides finalization of statements

```scala
case class LinkAst(appComps: List[AppVersionComp], stms: Array[Statement])
```

### 3. TypeLink

Handles type resolution and linking:

- Manages type resolution steps
- Handles properties linking
- Processes class extensions
- Maintains type hierarchy

```scala
object TypeLink {
  def apply(complete: DslType): TypeLink
  def apply(linker: DslLinker, origin: DslType, parentId: Option[DslId], relink: Boolean): TypeLink
}
```

### 4. DeclLink

Manages declaration linking:

- Handles declaration resolution
- Processes property linking
- Manages virtual mapping
- Handles extension declarations

```scala
object DeclLink {
  def apply(complete: Decl): DeclLink
  def apply(linker: DslLinker, origin: Decl, dslType: TypeLink, relink: Boolean): DeclLink
}
```

## Key Concepts

### Environment Availability

The DSL supports different environments:

- `Back`: Backend-only code
- `Front`: Frontend-only code
- `BackFront`: Code available in both environments

### Class Resolution

Classes are resolved through the `ClassResolver` which:

- Maintains a hierarchy of classes
- Handles package resolution
- Manages type references
- Supports generic types

### Type System

The type system includes:

- Basic types (classes, traits)
- Generic types
- Optional types
- Tuple types
- Query types

### Declaration Resolution

Declarations are resolved through:

- Self-type resolution
- Superclass traversal
- Property linking
- Extension handling

## Common Use Cases

### 1. Linking a DSL Expression

```scala
val result = DslLinker.linkExpr(
  envAvailability = EnvAvailability.BackFront,
  expr = someExpression,
  deps = dependencies
)
```

### 2. Resolving a Type Reference

```scala
val typeLink = classResolver.resolveWithFullName("core.SomeType")
```

### 3. Processing Properties

```scala
val props = DslProps(exprs).link(propertiesType)
```

## Error Handling

The linker provides comprehensive error handling through:

- `DslLinkException`: Base class for linking errors
- `DslClassNotFound`: When a referenced class cannot be found
- `DeclNotFound`: When a declaration cannot be resolved
- `SuitableDeclNotFound`: When no matching declaration is found
- `ExtensionNotFound`: When an extension cannot be found

## Best Practices

1. Always specify environment availability when linking expressions
2. Handle dependencies in the correct order
3. Use proper type resolution through ClassResolver
4. Implement proper error handling for linking failures
5. Follow the linking steps in the correct order (types → declarations → properties)

## Common Pitfalls

1. Not handling environment availability correctly
2. Missing dependencies in the linking process
3. Incorrect type resolution order
4. Not properly handling extensions
5. Missing error handling for linking failures

## Next Steps

For more advanced topics, consider exploring:

1. Generator types and their resolution
2. Complex type inference
3. Advanced property linking
4. Custom type extensions
5. Performance optimization techniques
