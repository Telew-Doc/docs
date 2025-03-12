# Collection Fields

Collection fields allow adding many items of similar type into an entity.

```dsl
entity Foo {
    field strings: [String]?
    field companies: [Company]?
}
```

In the example the `strings` field can contain many strings, the `companies` field is one to many reference field and can contain many companies.
In a collection field, you can also store composite structures when you need to have few fields linked to each other.

```dsl
entity Company { 
  field phones: [Phone]?
}

class Phone { 
  field countryCode: Int 
  field number: String 
}
```

!!! note
    You cannot use references inside classes.
    If you need this, you have to use entities instead and make the reference field inline.