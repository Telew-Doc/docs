# Fields Availability

## `ref`

When you load a form all fields of the current entity will be available. However, if you have a reference to another entity, this entity will have only a few fields loaded from the server.

To display a reference the system will use `ref view` and `title`. So if a field is used either in the `ref view` or in `title` calculation, it should be available on the client. To make sure this is the case you should mark the field with the `ref` modifier.

```dsl
entity Person {
    ref field firstName: String?
    ref field familyName: String
    impl func title = "$firstName $familyName"
}

entity Bug {
    impl field title: String
    ref field status: BugStatus
    impl view ref = row{status title}
}
```

It's not necessary to mark the `title` field with `ref` because the system will do it implicitly.

If you use a field in many computations it is better also to mark it as `ref` especially if it does not contain a lot of data. The computation will work anyway but the system will load full entity in a different call which will make it less performant.

```dsl
entity Product {   
    impl field title: String
    ref field price: Dec[2]
}

inline entity InvoiceItem {
    field product: Product
    field quantity: Dec[2]
    compute price = product.price
    compute amount = quantity * price
}
```


## `list`

If you load a list of items the system will not load all the fields to make it more performant. By default, it will not load collection and text fields. However, if you want to display such fields you can mark the field with `list` modifier.

```dsl
entity Task {
    impl field title: String
    list field description: Text
    impl object view list = Task.all >> nav {
        list {
            grid { title description }
        }
    }
}
```

All fields marked with the `ref` modifier are available in lists.

You can mark with `ref` or `list` modifier not only fields but also compute fields. It can be useful when you do not want to retrieve a collection from the server but only a result of computation:

```dsl
entity Foo {
    impl field title: String
    list compute createdBy = activities.first?.person
    impl object view list = Foo.all >> nav {
        table { title createdBy }
    }
}
```


## Availability order

There are several other availability statuses for fields defined inside DSL, and each of them has order value assigned to it.
Those statuses (from `6` to `-1`):

`Overall` > `Patch(entityId)` > `All` > `Inline` > `List` > `Ref` > `Nothing` > `NotInit`

When retrieving some data from fields you need to make sure that the requested fields ordering value is lower than the ordering value of the parent field. Example:

```dsl
entity PseudoPerson {
	field name: String
    field company: PseudoCompany
	impl func title: String = "Person: $name"
}

entity PseudoCompany {
	field name: String
	impl func title: String = "Company: $name"
}
```

In this example, when we will open `PseudoPerson` form we will see that `company` field won't show us company names properly inside selector list, and in console we will see following error:

```
Func calculating: Cannot update availability: com.erp.dsl.DslFieldUnavailableException: Field test.com.PseudoCompany@37146.185_180.name is unavailable: List > Ref
```

To fix this we can make name field to be `ref` inside `PseudoCompany` entity like this:

```dsl
entity PseudoCompany {
	ref field name: String
	impl func title: String = "Company: $name"
}
```

Now everything should work and in selector field for `PseudoPerson` we should see proper list of companies.