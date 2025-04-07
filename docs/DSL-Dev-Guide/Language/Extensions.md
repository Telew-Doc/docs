# Extensions

```dsl
entity Company {
    field name: String
}

extend entity Company {
    field description: String
}
```

You can add fields into existing entity or class using the `extend entity` construction. In this example, `Company` will have the `description` field as well as `name`. It allows to add user-specific fields into existing applications.