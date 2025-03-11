# Views

## `list`

It determines how to display list of entity items.

```dsl
entity Company {
    field code: Int
    field name: String
    impl object view list = Company.all >> nav {
        table { code, name }
    }
}
```

The `object` modifier means that this view does not have an instance of `Company` to display and should be started from a query. `Company.all` will select all companies. `nav` is a navigation layout and will create a navigation bar and filters panel. `table` will create a table with two columns `code` and `name`.


## `form`

A `form` view determines how one item will be shown to the user.

```dsl
entity Company {
    field code: Int
    field name: String
    impl view form = nav {
        grid {
            code
            name
        }
    }
}
```


## `ref`

A `ref` view allows to define how reference will look like in other entities. It can be useful if you want to display not only title but some additional information such as status.

```dsl
entity Bug {
    field title: String
    ref field status: BugStatus
    impl view ref = x { status title }
}
```

After this all references to `Bug` will have status and title in a row.
!!! warning 
    If you are using a field in a `ref` view you should add a `ref` keyword to the view so that the data will be available for the reference view.


## `refList`

When you define a `ref` view it will be user for references list in the selector as well. However you can use a different view if you want. For example if you want to use a table selector list:

```dsl
entity Product {
    field code: String
    field title: String
    impl view ref = y { title code }
    impl object view refList = Product.all >> table { title code }
}
```


## `traitItem`

This view will be used for a trait list to display a particular item.

```dsl
trait Issue {
    field title: String
}

entity Bug extends Issue {
    field severity: Severity
    view traitItem = grid { title severity }
}

entity UserStory extends Issue {
    field feature: Feature
    view traitItem = grid { title feature }
}
```
One `traitItem` view will be used to represent `Bug` entities and another for `UserStory` entities.
