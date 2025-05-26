# IIncomeType

**Type:** trait  
**App:** flow2b.product

**Extends:** [`IBasicProduct`](../flow2b_product/IBasicProduct.md)

**Implements:** `IProductTaxonomy`

## Fields

### `gstRate`

**Type:** `GstRate?`

**Modifiers:** ref

---

### `specialGstRate`

**Type:** `UPercent[2]?`

**Modifiers:** ref

---

### `getGstRate`

**Type:** `UPercent[2]??`

**Modifiers:** compute

---

### `nonTaxable`

**Type:** `UPercent?`

**Modifiers:** ref

---

### `taxable`

**Type:** `UPercent?`

**Modifiers:** compute

---

## Functions

### `collectPhotos`

**Returns:** `[Image]?`

**Modifiers:** override

---

### `isTangible`

**Modifiers:** impl

---

### `superCategory`

**Modifiers:** impl

---

### `subCategories`

**Modifiers:** impl

---

### `name`

**Modifiers:** impl

---

### `gstRate`

**Returns:** `UPercent[2]??`

**Modifiers:** override

---

