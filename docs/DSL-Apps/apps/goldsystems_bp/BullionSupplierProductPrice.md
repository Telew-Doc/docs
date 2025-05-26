# BullionSupplierProductPrice

**Type:** entity  
**App:** goldsystems.bp

**Modifiers:** inline

**Extends:** [`IStaticPrice`](../flow2b_product/IStaticPrice.md)

**Implements:** `IPriceSales`

## Fields

### `pricing`

**Type:** `BullionSupplierPricing inline by products`

**Modifiers:** system

---

### `percentMargin`

**Type:** `Percent?`

---

### `fixedMargin`

**Type:** `Money[currency]?`

---

## Functions

### `model`

**Modifiers:** impl

---

### `superProduct`

---

### `levels`

**Modifiers:** impl

---

### `salesPrice`

**Returns:** `Future[SalesPrice]`

**Modifiers:** impl

---

