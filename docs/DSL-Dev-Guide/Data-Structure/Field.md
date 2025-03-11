# Field

## Definition and examples

***Field*** represents some data that is stored in the database as a separate property.

```dsl
entity Company {
    ...
    field code: Int 
    field name: String 
    ...
}
```

Two fields are declared here for the entity `Company`: `code` and `name`. The code is an `Int` and name is a `String`.

---

## Naming conventions

    - use camelCase
    - use singular form of the word

!!! info "Same singular and plural rules apply as in [entities](Entity.md#naming-conventions)"

---

## Default Values

You can set a default value for a field:

```dsl
field name: String = “Default Name”
```

or

```dsl
field name: String {
    default = “Default Name”
}
```

If you have a default value, you can omit the data type declaration:

```dsl
field name = “Default Name”
```

This field will be considered `String` automatically because “Default Name” is `String`.
