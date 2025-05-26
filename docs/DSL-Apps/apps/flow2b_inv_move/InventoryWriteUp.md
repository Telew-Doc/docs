# InventoryWriteUp

**Type:** entity  
**App:** flow2b.inv.move

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `IProdQtyItem with FProductItemsInline with StockCorrection with IProdMoveIn with IProdMoveItemIn`

## Fields

### `stockType`

**Type:** `StockInvType`

**Modifiers:** ref

---

### `price`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `amount`

**Type:** `UMoney[currency]?`

---

## Functions

### `prodMoveIn`

**Modifiers:** impl

---

### `moveInItems`

**Modifiers:** impl

---

### `moveInDate`

**Modifiers:** impl

---

### `moveInState`

**Modifiers:** impl

---

### `moveInLE`

**Modifiers:** impl

---

### `moveInStore`

**Modifiers:** impl

---

### `moveInStockType`

**Modifiers:** impl

---

### `moveItemActive`

**Modifiers:** impl

---

### `currency`

**Modifiers:** override

---

### `title`

**Returns:** `String`

**Modifiers:** impl

---

### `journalDate`

**Returns:** `Date`

**Modifiers:** override

---

## Views

### `form`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

