# Compute Field

## Definition and examples

***Compute Field*** is similar to a [field](Field.md#definition-and-examples) but it's not stored in the database and instead is computed each time on demand.  
To declare a compute definition, use the `compute` keyword instead of `field` and set an expression for calculation.

```dsl
entity Invoice {
    ...
    field qty: Dec[2]
    field total: Dec[2]
    compute price: Dec[2] = total / qty
    ...
}
```

Here we declare the compute field `price`. You can simplify the declaration and omit the datatype, it will be inferred automatically:

```dsl
compute price = total / qty
```

This compute field will be read only. If you want to make it editable, you have to use the `update` modifier:

```dsl
compute price {
    value = total/qty
    update = { total = qty*price }
}
```

??? question "What's a `value` modifier here"
    Same as with any [field](Field.md#default-values) you can set the default value (in our case a function to compute it)
    using syntax as above. In case of `compute` fields it's just named `value` instead of `default`

This means that when the price field is changed, we will update total with `qty * price`.
