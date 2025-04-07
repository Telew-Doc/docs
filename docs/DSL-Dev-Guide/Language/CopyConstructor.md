# Copy Constructor

You can create one item based on another. If the name of fields and data type of the field are the same it will copy the data. It helps to write less code:

```dsl
entity Foo {
    field a: Int
    field b: Int
    field c: Int
    field d: Int
}

entity Bar {
    field a: Int
    field b: Int
    field c: String
}
```

Then if we have a `Foo` and want to make a `Bar` we can write:

```dsl
Bar(foo)
```

It's similar to:

```dsl
Bar(a = foo.a, b = foo.b)
```

It will not copy `d` because it does not exist in `Bar` and it will not copy `c` because data type is different but you can make it explicitly if you want:

```dsl
Bar(foo, c = foo.c)
```