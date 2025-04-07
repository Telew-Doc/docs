# Inheritance

```dsl
trait HasCode extends Entity { 
    field code: String 
} 

trait ActionItem extends Entity { 
    func name: String 
    field priority: Int 
    field status: Status 
} 

entity Product extends HasCode { 
    field description: Text?
    impl func title = code
} 

entity Company extends HasCode with ActionItem { 
    impl field name: String 
    impl func title = name
}
```

Traits can be a base for entities and classes. An Entity can inherit multiple traits. All fields declared in the traits will be available in the entity. A Product will have `code` field declared in the `HasCode` trait. It declares also `description` field. So it will have these two fields.

In this example, the `Company` entity will have:
- `code` field from `HasCode` trait
- `priority` and `status` from `ActionItem`
- `name` field declared in the `Company`

In `ActionItem`, `name` is declared as `func`. This means that the trait itself does not create a field but requires from entity to provide either a field, compute field or a function with the same signature. This is more flexible and allows to use existing fields to calculate the value and satisfy the trait's requirements.

It allows to avoid duplication and reuse the same structure in similar entities. It also allows defining a contract which entities should satisfy when implementing this trait.

Classes cannot implement traits and you have to use an interface instead.

## Impl and Override

`impl` modifier is used when the function is declared in a superclass but not implemented:

```dsl
impl func foo = 20
```

`override` modifier should be used if the function is implemented in a superclass:

```dsl
override func foo = 20
```

A function is considered declared, not implemented and the `impl` modifier should be used if:

1. A function is not implemented:
    ```dsl
    func foo: Int
    ```

2. A function is implemented with a constant:
    ```dsl
    func foo: Int = 10
    ```

3. A function is implemented with a default property:
    ```dsl
    func foo: Int {
        default value = bar
    }
    ```

The `override` modifier should be used if a function is implemented in any other way:

```dsl
func foo: Int = bar
```