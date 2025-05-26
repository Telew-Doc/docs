# ProductAltUnit

**Type:** entity  
**App:** flow2b.product

**Modifiers:** inline

**Extends:** [`TWeightSize`](../flow2b_product/TWeightSize.md)

## Fields

### `product`

**Type:** `IAltUnits by altUnits`

**Modifiers:** ref

---

### `baseUnit`

**Type:** `ProductUnit`

**Modifiers:** compute

---

### `unit`

**Type:** `ProductUnit`

**Modifiers:** ref

---

### `baseK`

**Type:** `UQty[baseUnit]`

**Modifiers:** ref

---

### `unitK`

**Type:** `UQty[unit]`

**Modifiers:** ref

---

### `k`

**Type:** `UDec[8]`

**Modifiers:** compute

---

