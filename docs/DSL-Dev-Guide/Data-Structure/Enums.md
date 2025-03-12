# Enums

If you have a fixed set of variants to choose, it is recommended to use an `enum` field.

```dsl
enum TransactionType { 
    case Invoice 
    case Sale 
} 

entity Transaction { 
    field type: TransactionType 
}
```

`TransactionType` is an `enum` class, and you can see field type is an `enum` field. TransactionType contains to cases Invoice and Sale. This field will be displayed to use as a combo box and the user will be able to select an option either `Invoice` or `Sale`. Conventionally, cases should use PascalCase.

To provide a text which user will see you can write it as in the example or use label modifier as usual.

```dsl
enum TransactionType {
    case Invoice = “Customer Invoice”
    case Sale = “We Sale”
}
```

If you put your enum type in square brackets, user will be able to choose few options together.

```dsl
enum Tag {
    case Tag1
    case Tag2
    case Tag3
}

entity Company {
f   ield tags: [Tag]
}
```

Enums can have parameters. You can use it as a table with predifined data.

```
enum ClientCategory(discount: Dec[2]) {
    case Basic(discount = 0)
    case Premium(discount = 0.1)
}

entity Company {
    field category: ClientCategory
    func discount = category.discount
}
```