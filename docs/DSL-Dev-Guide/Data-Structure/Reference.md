# Reference

## Definition and examples

***Reference*** field contains a reference to another or the same entity.
To do this, you can easily use the name of the entity as data type after colon:

```dsl
entity Invoice {
    field company: Company
}

entity Company { ... }
```

You can make references to any entities. Be aware that by default in UI string representation of the referenced entity will be used taken from `title` definition.
Make sure that you define it properly:

```dsl
entity Company {
  ref field code: Int
  ref field name: String
  impl func title: String = "$code | $name"
}
```

!!! danger "High risk of getting `Untitled` here"
    You've probably noticed the use of `ref` keyword in this example.
    While it's not necessary for defining references between entities (or even base types as seen here)
    its use is required here, as without it you'll most likely see the `Untitled` being displayed instead of the intended reference.
    It's not clear exactly why, most likely definitions with `ref` have better availability internally and can be fetched by front-end
    when extracting `title`.

By default, a selector will show only the title field. However, you can set a custom layout. For this, you should declare `ref` view.

```dsl
entity Company {
    ref field code: String
    impl field title: String
    impl view ref = y { title code }
}
```

After this, all references to the Company entity will show the code field under the title field.
The same layout will be also used in a selector list. But you can customise this as well as providing a refList view.

```dsl
entity Company {
    ref field code: String
    impl field title: String
    impl view ref = column { title code }
    impl object view refList = Company.all >> table {title, code}
}
```

Now selector will show a table with two columns instead of list of the ref layout.

---

## Reference modes

References can work in three modes:


### edit

This is a default mode and it means that user can select a reference.


### read

This creates a read only reference field. A usual use case is backward reference like in the example:

```dsl
entity Invoice {
    field client: Company
    ...
}

entity Company {
  field invoices: [Invoice] read by client
  ...
}
```

In this case, a user will not be able to choose an existing invoice and assign it to a company but he will be able to see all invoices for the company and add a new invoice.


### inline

Inline references will look similar to an embedded field. It works well if you want to create a connection between entities with some attributes:

```dsl
entity Person {
    field roles: [OrganisationPersonRole] inline by person
    ...
}

entity Organisation {
    field employees: [OrganisationPersonRole] inline by organisation
    ...
}

inline entity OrganisationPersonRole {
    field person: Person
    field organisation: Organisation
    field role: String
    field startDate: Date
    field endDate: Date?
}
```

Actions like deletion / restoration are propagated by default from the object contained in the inline field onto the host object. So, from the example above, if an `OrganisationPersonRole` object is deleted, its `Person` will be deleted too. Same for restoration action. To prevent this propagation, `touchCascade` property can be used:

```dsl
entity Person { 
    field roles: [OrganisationPersonRole] inline by person {
        touchCascade = false
    }
}
```

That way, when the object contained in the roles field is deleted, the corresponding person will not be deleted.

---

## Bidirectional references

When you have a reference in one direction, sometimes you would like to easily find items which refer to this item. To achieve this you have to declare a backward reference field and using the `by` modifier link two reference fields together. Then the system will keep them in sync.

```dsl
entity Invoice {
    field company: Company
}

entity Company {
    field invoices: [Invoice]? by company
}
```

In the example, invoices have a company reference. In the Company entity, the invoices backward reference is declared.
