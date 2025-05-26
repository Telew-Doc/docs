# SalesItem

**Type:** entity  
**App:** flow2b.inv.order

**Modifiers:** inline

**Extends:** [`ISalesItemWithDelivery`](../flow2b_inv_order/ISalesItemWithDelivery.md)

**Implements:** `OrderProductItem with FProductItems`

## Fields

### `productBaseCost`

**Type:** `ProductCost?`

**Modifiers:** compute

---

### `productCost`

**Type:** `Future[ProductCost?]`

**Modifiers:** compute

---

### `approxCost`

**Type:** `Unknown`

**Modifiers:** compute

---

### `costDate`

**Type:** `Date?`

**Modifiers:** compute

---

### `cost`

**Type:** `Future[UMoney[currency]?]`

**Modifiers:** compute

---

### `margin`

**Type:** `Future[Percent[2]?]`

**Modifiers:** compute

---

## Functions

### `itemsQty`

**Modifiers:** impl

---

### `needProductItems`

**Modifiers:** impl

---

### `stockProd`

---

### `revenueLedgers`

**Modifiers:** impl

---

### `dekit`

**Returns:** `Future[Void]`

---

## Views

### `rowView`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

