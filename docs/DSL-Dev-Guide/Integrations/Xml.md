# XML

## Serialization

Use function `xml`. For example:

```dsl
class Foo {
    field bar: String
    field baz: Int
}

Foo(bar = "Test", baz = 10).xml
```

It will give:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<foo>
    <bar>Test</bar>
    <baz>10</baz>
</foo>
```

## Attributes vs Elements

By default fields are serialized as elements.

```dsl
class Foo {
    xml = Attribute
    field bar: String
    field baz: Int
}

Foo(bar = "Test", baz = 10).xml
```

It will give:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<foo bar="Test" baz="10"></foo>
```

You can also specify attributes for individual fields:

```dsl
class Foo {
    field bar: String
    field baz: Int {xml = Attribute}
}

Foo(bar = "Test", baz = 10).xml
```

Result:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<foo baz="10">
    <bar>Test</bar>
</foo>
```

## Name

You can customize element names using `extName`:

```dsl
class Foo {
    extName = "fooTag"
    field bar: String {extName = "barName"}
    field baz: Int
}

Foo(bar = "Test", baz = 10).xml
```

Result:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<fooTag>
    <barName>Test</barName>
    <baz>10</baz>
</fooTag>
```

## Namespaces

You can define XML namespaces:

```dsl
class Foo {
    xmlNamespaces = [
        "ns1" -> "https://test.com/ns1",
        "ns2" -> "https://test.com/ns2"
    ]
    xmlNamespace = "ns1"
    field bar: String 
    field baz: Int {xmlNamespace = "ns2"}
}

Foo(bar = "Test", baz = 10).xml
```

Result:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<ns1:foo xmlns:ns1="https://test.com/ns1" xmlns:ns2="https://test.com/ns2">
    <ns1:bar>Test</ns1:bar>
    <ns2:baz>10</ns2:baz>
</ns1:foo>
```

If you want to use or refer to the default namespace, use an empty string.

## Mapping

You can transform values during serialization:

```dsl
class Foo {
    field baz: Int {extMap(_*33)}
}

Foo(baz = 10).xml
```

Result:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<foo>
    <baz>330</baz>
</foo>
```

## Deserialization

You can deserialize XML with namespaces:

```dsl
class Foo {
    xmlNamespaces = [
        "ns1" -> "https://test.com/ns1",
        "ns2" -> "https://test.com/ns2"
    ]
    xmlNamespace = "ns1"
    field bar: String 
    field baz: Int {xmlNamespace = "ns2"}
}

val xmlString = '''
<?xml version="1.0" encoding="UTF-8"?>
<x:foo xmlns:x="https://test.com/ns1" xmlns:y="https://test.com/ns2">
    <x:bar>Test</x:bar>
    <y:baz>10</y:baz>
</x:foo>
'''

xmlString.parseXml[Foo]
```

Namespace prefixes can differ - the URI is what's considered.

## Selectors

If you have a complicated XML structure but need to extract a little data, you can use selectors instead of deserialization:

```dsl
xmlString
    .parseXml[XmlElement]
    .select("@foo").onlyOne?.value
```

You need to parse XML into the `XmlElement` class. Then you can use the `select` function to select a list of `XmlElement` and `value` to get the string value.

```dsl
back class XmlElement {
    native select(selector: String?): [XmlElement]?
    native value: String?
}
```

You can find the selector's syntax here:
[XPath Selector Syntax](https://docs.oracle.com/javase/6/docs/api/javax/xml/xpath/package-summary.html)
