# Optional

If a field is ***optional***, you have to mark it explicitly, otherwise, the system will force a user to fill the field in.

```dsl
entity Company { 
    impl field title: String 
    field notes: String? 
}
```

The system will force a user to fill the title field here but notes can be empty.

!!! danger "Quirks"
    While developing with DSL you'll probably encounter some examples of confusing behavior involving this feature:

    - Some types have values that will default to `None`, i.e. missing value. E.g. for `String`s the empty string `""` will be treated as `None`, and for most numeric types `0` will be treated as `None` as well, for all collections empty collection `[]` will be treated as `None` too.
    - Plenty of optional values exist within existing DSL ecosystem and you'll inevitably will have to interact with them. Unfortunately sometimes the compiler goes crazy and issues errors for incompatible types because it expects optional value to be passed / thinks that the value you're working with is optional / nests several optionals resulting in `String???` data types etc.  
    If you are sure it's not a program error you can explicitly cast to / from optional values using `!` (to remove optional type) or `?` (to assume optional type). E.g. `#!dsl definitelyDefinedField!.someFunc(...)`, `#!dsl SomeEntity.someMethod(definitelyDefinedField!)` or `#!dsl couldBeOptional?.someValue`, `#!dsl SomeEntity.methodWithOptionalArg(couldBeOptional?)` etc.
