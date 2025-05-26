# DevQuoteItem

**Type:** entity  
**App:** flow2b.net.sales

**Extends:** [`PseudoEntity`](../core/PseudoEntity.md)

## Fields

### `quote`

**Type:** `DevQuote`

**Modifiers:** ref

---

### `salesItem`

**Type:** `SalesItem?`

**Modifiers:** system

---

### `issues`

**Type:** `[Issue]? by quotes`

---

### `adds`

**Type:** `[DevQuoteItemAdd]? inline by item`

---

### `estimation`

**Type:** `Estimation?`

**Modifiers:** compute

---

### `margin`

**Type:** `UPercent[2]?`

---

### `_desc`

**Type:** `Text?`

---

### `desc`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `mainEntity`

**Modifiers:** impl

---

### `ready`

---

### `makeItem`

**Returns:** `Void`

**Modifiers:** back

---

### `amount`

**Returns:** `UMoney[quote.currency]?`

---

## Views

### `ref`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

