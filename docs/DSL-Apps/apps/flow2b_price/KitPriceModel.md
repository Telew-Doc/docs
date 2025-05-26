# KitPriceModel

**Type:** entity  
**App:** flow2b.price

**Extends:** [`IDynamicPriceModel`](../flow2b_product/IDynamicPriceModel.md)

**Implements:** `IProdFilterOwner with IPriceModOwner`

## Fields

### `rules`

**Type:** `[KitModelRule]? inline by model`

---

### `rounding`

**Type:** `Rounding?`

---

### `discount`

**Type:** `Percent[2]?`

---

## Functions

### `title`

**Modifiers:** impl

---

### `priority`

**Returns:** `Dec[8]?`

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

