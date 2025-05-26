# SaleCampaign

**Type:** entity  
**App:** flow2b.price

**Extends:** [`IDynamicPriceModel`](../flow2b_product/IDynamicPriceModel.md)

## Fields

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `rounding`

**Type:** `Rounding?`

---

### `rules`

**Type:** `[SaleCampaignRule] inline by campaign`

---

### `saleCategories`

**Type:** `[IProductCategory]?`

**Modifiers:** ref

---

### `saleTags`

**Type:** `[IProductTag]?`

**Modifiers:** ref

---

## Functions

### `priority`

**Returns:** `Dec[8]?`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `isRentModel`

**Modifiers:** impl

---

### `doPrice`

**Returns:** `IPrice?`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

