# Queries

Every function's description will use the sample data to show its result.

```dsl
entity Invoice {
    field number: String
    field total: Dec[2]
    field items: [InvoiceItem] inline by invoice
}

entity InvoiceItem {
    field invoice: Invoice
    field product: String
    field amount: Dec[2]
}
```

## Sample Data

### Invoice:
```
number    total
1           100
2           200
```

### InvoiceItem:
```
invoice    product    amount
1          p1             70
1          p2             30
2          p2            200
```

## Query Functions

### `all`

To select all items for entity. Usually a query will be started from all items for an entity.

```dsl
Invoice.all
```

Result:
```
number    total
1    100
2    200
```

### `filter`

Filter invoices with total more than 100.

```dsl
Invoice.all.filter(total > 100)
```

Result:
```
number    total
2           200
```

### `find`

Find return the first item satisfied the condition if it exists.

```dsl
Invoice.all.find(total > 100)
```

Result:
```
number = 2
total = 200
```

### `exists`

It returns true if there is an item which satisfies the condition.

```dsl
Invoice.all.exists(total > 100)
```

Result:
```
true
```

### `map`

```dsl
Invoice.all.map(total, foo = total2, bar = total3)
```

Result:
```
total    foo    bar
100    200    300
200    400    600
```

It takes every item in the query and returns a new according to the expressions.

### `flatMap`

```dsl
query = Invoice.all.flatMap(items)
```

Result:
```
invoice    product    amount
1    p1    70
1    p2    30
2    p2    200
```

It is working the same way as map, but instead of returning collection of collections, it joins the collections together.

```dsl
Invoice.all.map(items)
```

Result:
```
items
invoice    product    amount
1          p1             70
1          p2             30
invoice    product    amount
2          p2            200
```

### `*.`

This is a shortcut syntax for map or flatMap if you return only one field.

```dsl
Invoice.all*.total 
```

Result:
```
total
100
200
```

Query:

```dsl
Invoice.all*.items
```

Result:
```
invoice    product    amount
1    p1    70
1    p2    30
2    p2    200
```

### `groupBy`

It groups items with provided key. Usually it is used along with the agg.

```dsl
InvoiceItem.all.groupBy(product)
```

Result:
```
product 
p1 
    invoice    product    amount
    1          p1             70
p2 
    invoice    product    amount
    1          p2             30
    2          p2            200
```

### `agg`

It aggregated previously grouped results.

```dsl
InvoiceItem.all.groupBy(product).agg(amount.sum)
```

Result:
```
product    amount
p1             70
p2            230
```

### `accum`

Cumulative sum.

```dsl
Invoice.all.accum(acc = total.sum)
```

Result:
```
number    total    acc
1           100    100
2           200    300
```

### `sortBy`

Sort items in the query.

```dsl
InvoiceItem.all.sortBy(product.title, amount.desc)
```

In the example, we sort by product title. If the title is the same then we by amount in a reverse order (descending).

Result:
```
invoice    product    amount
1          p1             70
2          p2            200
1          p2             30
```
