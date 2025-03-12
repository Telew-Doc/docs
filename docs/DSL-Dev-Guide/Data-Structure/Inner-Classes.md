# Inner Classes

You can declare inner classes. Then you will be able to access the parent class fields.

```dsl
entity Company {
    field countryCode: Int
    field phones: [Phone]

    class Phone {
        field countryCode: Int = this[Company].countryCode
        field number: String
    }
}
```

In this example, we set the `countryCode` code default value to the same value as in the company but the user will be able to change it.