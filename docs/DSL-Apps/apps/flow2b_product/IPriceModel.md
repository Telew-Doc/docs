# IPriceModel

**Type:** trait  
**App:** flow2b.product

**Extends:** [`RefEntity`](../core/RefEntity.md)

**Implements:** `IIPriceModel with HasN`

## Fields

### `levels`

**Type:** `[IPriceLevel]?`

**Modifiers:** ref

---

### `levelTitles`

**Type:** `String?`

**Modifiers:** compute

---

### `canceled`

**Type:** `Bool`

---

### `vendor`

**Type:** `IVendor by priceModels`

**Modifiers:** ref

---

## Functions

### `start`

**Returns:** `Date`

---

### `end`

**Returns:** `Date?`

---

### `numPrefix`

**Modifiers:** impl

---

### `nextN`

**Modifiers:** impl

---

### `hasLevel`

**Returns:** `Bool`

**Modifiers:** impl

---

### `isDefaultLevel`

---

### `mainPriceLevel`

---

### `buttonLabel`

**Returns:** `String`

---

### `isOur`

**Returns:** `Bool`

---

### `calcState`

**Returns:** `PriceModelState`

---

### `ours`

**Returns:** `[IPriceModel]?`

**Modifiers:** object

---

### `theirs`

**Modifiers:** object

---

### `models`

**Returns:** `[IPriceModel]?`

**Modifiers:** object

---

### `touchAllProducts`

**Returns:** `Void`

**Modifiers:** back

---

## Views

### `traitItem`

**Modifiers:** impl

---

### `pmNavButtons`

---

