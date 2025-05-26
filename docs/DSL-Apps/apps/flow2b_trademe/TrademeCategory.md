# TrademeCategory

**Type:** entity  
**App:** flow2b.trademe

## Fields

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `number`

**Type:** `String?`

---

### `path`

**Type:** `String?`

**Modifiers:** ref

---

### `subcategories`

**Type:** `[TrademeCategory]? by supercategory`

---

### `supercategory`

**Type:** `TrademeCategory? by subcategories`

---

### `areaOfBusiness`

**Type:** `AreaOfBusiness`

---

### `hasClassifieds`

**Type:** `Bool`

---

### `canHaveSecondCategory`

**Type:** `Bool`

---

### `canBeSecondCategory`

**Type:** `Bool`

---

### `count`

**Type:** `Int?`

---

## Functions

### `title`

**Modifiers:** impl

---

### `all`

**Returns:** `[TrademeCategory]?`

---

