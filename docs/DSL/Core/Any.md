# Any


## Overview

**Type**: interface

!!! note "Seemingely everything on our platform inherits this ***implicitly***"


## Functions

### `toString`

**Returns**: `String?`  
**Default implementation**: `""`

Self-explanatory, base classes (`Entity`, `Enum` etc) implement this already so unless your case is special you won't need to touch this.


## Views

### `form`

No default implementation.

!!! note "Seems like this view is still auto-generated outside of DSL so it doesn't need to explicity defined anyway unless required"


## Object Native Functions


### `interface`

**Returns**: `Dsl`

Returns almost all definitions of this construct, including everything from extended constructs.

**Example**:

- Query: `#!dsl AnyRef.interface`
- Result:
    ```dsl
    // interface core.AnyRef extends Any with Any
    native fullTitle(): String
    native get(Param(187,field,String)): T
    native update(Param(189,field,String), Param(190,value,Any)): Ref
    native default(Param(193,field,Ref => R)): R
    native defaultAllField(): Void
    native clear(Param(197,field,Ref => R)): R?
    native updated(Param(199,field,Ref => Any)): Bool
    native origin(Param(202,field,Ref => R)): R
    native validationErrors(): [String]?
    native increment(Param(205,field,Ref => Int?)): Int?
    native silentUpdate(Param(208,field,Ref => R), Param(209,value,R)): R
    native rollback(): Ref
    native json(): Json
    native xml(): Xml
    native toMap(): [String: Any]?
    native dslType(): DslType

    // interface core.Any extends 
    func toString(): String?
    view form
    ```

!!! note
    As any entity can be extended further by other DSL apps, depending on which workspace you invoke this command from you might get different results.

!!! danger
    As can be seen in example, this output doesn't include `object` definitions for some reaosn, not sure if this can be achieved.


### `hierarchy`

**Returns**: `Text`

Returns everything that this construct extended or extends, all super- and subtypes.

**Example**:

- Query: `#!dsl ImportTask.hierarchy`
- Result:
    ```dsl
    trait core.ImportTask

    Extends:
    core.Entity

    All Supertypes:
    core.Entity, core.RefEntity, core.AnyEntity, core.AnyRef, core.Any

    Extended by:
    flow2b.bank.BankStatementUpload, core.Import, flow2b.order.parse.OrderImport

    All Subtypes:
    flow2b.bank.BankStatementUpload, core.Import, flow2b.order.parse.OrderImport
    ```

!!! note
    As any entity can be extended further by other DSL apps, depending on which workspace you invoke this command from you might get different results.


### `subObjects`

**Returns**: `#!dsl Set[this.object]?`


### `implObjects`

**Returns**: `#!dsl Set[this]?`