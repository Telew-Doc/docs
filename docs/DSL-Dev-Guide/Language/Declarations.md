# Declarations

## Top Level Declarations

On the top level of the file you can declare classes of different types:

### Entity

An entity will be stored in the database directly and will have an id. You can makes queries on this.

### Trait

Traits contain something common for few entities. Entities can implement many traits. You can select all items of entities which implement this trait.

### Class

A universal class that can contain fields, function, etc as well as entity, but it can be stored in the database only as an embedded entity field or collection field. You cannot select them directly only through its parent entity. You cannot have reference fields inside a class.

### Interface

Interface are similar to traits but it can be implemented by classes as well as entities and you cannot select data for interface.

### Report

Declares report.

### Enum

Enum is a datatype which can have only few values. For example statuses.

### Access

Declares an access group.

### Menu

Declares a menu.

## Lower Level Declarations

Inside the top level declarations you can declare:

### Field

Fields are something which will stored in database.

### Func

A function. Function can have parameters and return a value.

### Compute

Compute fields are not storing in the database by default but they are shown to user as a field.

### Class

Inner class. Instance and fields of the current class are available inside the inner class.

### View

Declare a form or list view. Object related.

### Case

Case for enum. Object related.

### Style

Declare a style. Object related.

### Entity

Describe an entity access for access groups or entity reference in menu. Object related.

### Query

Defines a query.

## Declaration Modifiers

With declarations you can use some modifiers:

### Native

This means that the function is implemented in native code and here this is only a description for the function.

### Object

Make this function related to object not to instance. This means that you cannot use other instance related declaration in this function. But you can use this function without an instance.

```dsl
class Foo {
    field instanceField: Int 
    func instanceFunc: Int = instanceField
    object func objectFunc: Int = 22 
    object func objectFunc2: Int = instanceField //!!!Error. You cannot use instance declarations here
}

Foo.objectFunc
Foo.instanceFunc //!!!Error. You cannot call it without an instance
```