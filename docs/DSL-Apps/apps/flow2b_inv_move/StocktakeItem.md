# StocktakeItem

**Type:** entity  
**App:** flow2b.inv.move

**Modifiers:** inline

**Extends:** [`InlineEntity`](../core/InlineEntity.md)

**Implements:** `FProductItems with IProdUnit`

## Fields

### `stocktake`

**Type:** `Stocktake by items`

---

### `barcode`

**Type:** `String?`

**Modifiers:** system

---

### `qty`

**Type:** `UQty[unit]?`

---

### `cost`

**Type:** `UMoney[currency]?`

---

### `costPrice`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `baseQty`

**Type:** `UQty[product.unit]?`

**Modifiers:** compute

---

### `difference`

**Type:** `Qty[product.unit]?`

**Modifiers:** compute

---

## Functions

### `stockProd`

---

### `itemsQty`

**Modifiers:** impl

---

### `needProductItems`

**Returns:** `Bool`

**Modifiers:** impl

---

### `isDelivered`

---

### `currency`

**Returns:** `Currency`

---

### `labelsQty`

**Modifiers:** override

---

