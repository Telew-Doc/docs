# Entity

## Definition and examples

***Entity*** is something that will be stored in the database.

```dsl
entity Company { 
  impl field title: String 
}
```

Here `Company` is the name of the entity, `title` is a field of type `String`.

!!! info
    You can technically omit the `impl` modifier here, but it'll result in a compilation warning
    since all DSL entities are inhereting the title function `#!dsl func title: String`.

    ??? tip "Why `title` is an important definition"
        Apart from being used in the front-end for displaying the title for currently viewed entity
        this definition basically acts as a `toString` method for other parts of our UI (e.g. when displaying references)
        and even backend logic (when working with strings this definition will be used implicitly if necessary)

    ??? question "Why `field` if inhereting `func`"
        You can swap inherited properties to any other type: `field` | `compute field` | `function`

---

## Naming conventions

  - use PascalCase
  - use singular form of the word

!!! info "Plural form for use in front-end is auto-generated"
    It's also possible to explicitly define both singular and plural forms that will be displayed for this entity:  
    
    ```dsl
    entity Company {
        ...
        singular = "Company"
        plural = "Companies"
        ...
    }
    ```

---

!!! note "TODO"
    Fields
    Compute Fields
    Functions
    Views