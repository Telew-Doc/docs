# JSON

## Serialization

Every class or entity can be serialized to JSON or deserialized from JSON.
Use function `json`. For example:

```dsl
class Foo {
    field bar: String
    field baz: Int
}

Foo(bar = "Test", baz = 10).json
```

It will give:

```json
{
    "bar": "Test",
    "baz": 10
}
```

## Deserialization

You can deserialize `String` or `Data` with `parseJson` function:

```dsl
class Foo {
    field bar: String
    field baz: Int
}

'{
    "bar": "Test",
    "baz": 10
}'.parseJson[Foo] == Foo(bar = "Test", baz = 10)
```

If you deserialize into entity you can use key fields to make sure that the item is unique. If a key field is presented, it will search for the item with the same key. If it exists it will update other fields, if it doesn't a new item will be created.

```dsl
entity Product {
    field title: String
    key system field externalId: Int?
}
```

## Capitalization

C# based product uses capitalized field names. You can use class modifier `jsonCapitalizeFieldNames`:

```dsl
class Foo {
    jsonCapitalizeFieldNames = true
    field baz: Int
}

Foo(baz = 10).json
```

The result will be:

```json
{
    "Baz": 10
}
```

## JSON Name

You can set a field name other than the field name with `extName` field modifier:

```dsl
class Foo {
    field baz: Int {extName = "otherName"}
}

Foo(baz = 10).json
```

Result:

```json
{
    "otherName": 10
}
```

## Required Fields

If a field is not required and empty by default it will not be included in JSON:

```dsl
class Foo {
    field baz: Int?
}

Foo(baz = 0).json
```

Result:

```json
{}
```

However, you can use `extRequired` modifier to make it always present:

```dsl
class Foo {
    field baz: Int? {extRequired}
}

Foo(baz = 0).json
```

Result:

```json
{
    "Baz": 0
}
```

## Ignored Fields

If you do not want a field to be included in JSON, use `jsonIgnore` modifier:

```dsl
class Foo {
    field bar: String {jsonIgnore}
    field baz: Int
}

Foo(bar = "Test", baz = 10).json
```

Result:

```json
{
    "baz": 10
}
```

## JSON Mapping

If you want to use a different value than what's in the field when serializing or deserializing, you can use the `Mapper` interface or shorter `jsonMap` modifier:

```dsl
class Foo {
    field bar: Bar {jsonMap = BarMapper}
}

enum Bar(id: Int) {
    case Bar1(id = 1)
    case Bar2(id = 2)
}

object BarMapper extends Mapper[Bar, Int] {
    func apply(f: Bar): Int = f.id
    func unapply(f: Int): Bar = Bar.all.find(id == f)!
}

Foo.bar(bar = Bar2).json
```

Result:

```json
{
    "bar": 2
}
```

You can write the same thing shorter:

```dsl
class Foo {
    field bar: Bar {
        jsonMap(apply = id, unapply = v => Bar.all.find(id == v)!)
    }
}
``` 