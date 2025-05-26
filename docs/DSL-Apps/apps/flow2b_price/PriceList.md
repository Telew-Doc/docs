# PriceList

**Type:** entity  
**App:** flow2b.price

**Extends:** [`IStaticPriceModel`](../flow2b_price/IStaticPriceModel.md)

## Fields

### `pricesIncludingGst`

**Type:** `Bool`

**Modifiers:** ref

---

### `clearanceCategories`

**Type:** `[IProductCategory]?`

**Modifiers:** ref

---

### `clearanceTags`

**Type:** `[IProductTag]?`

**Modifiers:** ref

---

### `products`

**Type:** `[PriceListProduct]? inline by priceList`

---

## Functions

### `title`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `supports`

**Returns:** `Bool`

**Modifiers:** impl

---

### `findPrice`

**Modifiers:** impl

---

### `forceNewPrice`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

