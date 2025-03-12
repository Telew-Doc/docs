# Registers

`Register` is a stored accumulated linked list. It's used to make complex computation and get result with a close constant time not dependant on amount of data in the register.

## Example
For example `register` for simple stock calculations:

```dsl
register StockRegister {
    key field product: Product
    order field date: Date
    field qty: Qty
    stored compute stock: Qty? = prev?.stock + qty
}
```

Here it will accumulate stock by the key field product so you can get stock per product. `prev` is a link to the previous register item by date for the product. You can write information to the register from any entity or inline entity with `register` field:

```dsl
entity Purchase {
    field date: Date
    field product: Product
    field qty: Qty
    register stock = StockRegister(product = product, date = date, qty = qty)
}

entity Sales {
    field date: Date
    field product: Product
    field qty: Qty
    register stock = StockRegister(product = product, date = date, qty = -qty)
}
```

To get current stock for product: `#!dsl StockRegister.current`
To get stock for a particular date: `#!dsl StockRegister.at(date)`

If we create `#!dsl Purchase(date = Date("2016-01-05”), product = prod1, qty = 10)` a register item will be created with the same data and stock will be calculated as 10 because `prev` will be empty in this case.

`#!dsl Sales(date = Date("2016-01-10”), product = prod1, qty = 3)` another register item will be created here. `prev`, in this case, will be the previous register item with 10 in stock. So result in stock will be 10 - 3 = 7. `StockRegister.current` will return the last item only with 7 in stock.

If we create something before items already created the next items will be recalculated. For example, we forgot to create an earlier purchase but we can still do it: `#!dsl Purchase(date = Date("2016-01-01”), product = prod1, qty = 2)`. In this case, a register item will be created. `prev` will be empty and `stock` will be 2. next will be the first purchase and the register item will be recalculated giving 12 in stock. Then it will recalculate the item for sales and it gives 9 in stock.

If you create a purchase for another product `#!dsl Purchase(date = Date("2016-01-10”), product = prod2, qty = 5)` the `prev` will be empty and stock will be 5 for `prod2`. Stock for `prod1` will stay 9. `StockRegister.current` will return two items: `prod1` - 9 and `prod2` - 5.
