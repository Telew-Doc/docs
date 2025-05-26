# Brand

**Type:** entity  
**App:** flow2b.product

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `IProductTaxonomy with IProductAttrTerm`

## Fields

### `logo`

**Type:** `Image?`

---

### `actors`

**Type:** `[Actor]?`

---

### `superBrand`

**Type:** `Brand? by subBrands`

---

### `subBrands`

**Type:** `[Brand]? read by superBrand`

---

### `products`

**Type:** `[ISuperProduct]? by brands`

---

## Functions

### `attrName`

**Modifiers:** override

---

### `photos`

**Returns:** `[Image]?`

**Modifiers:** impl

---

### `superCategory`

**Modifiers:** impl

---

### `subCategories`

**Modifiers:** impl

---

### `taxonomyProducts`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

