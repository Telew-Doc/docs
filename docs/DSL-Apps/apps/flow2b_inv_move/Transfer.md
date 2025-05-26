# Transfer

**Type:** entity  
**App:** flow2b.inv.move

**Extends:** [`IProdMoveOut`](../flow2b_inv_move/IProdMoveOut.md)

**Implements:** `IProdMoveIn with Journal with HasN with IProdMovePath with FPathDates`

## Fields

### `sourceStockType`

**Type:** `StockType`

---

### `destinationStockType`

**Type:** `StockType`

---

### `state`

**Type:** `PathState`

**Modifiers:** ref

---

### `currency`

**Type:** `Currency`

---

### `toLegalEntity`

**Type:** `OurLegalEntity?`

---

### `source`

**Type:** `IStore`

**Modifiers:** ref

---

### `destination`

**Type:** `IStore`

**Modifiers:** ref

---

### `items`

**Type:** `[TransferItem]? inline by delivery`

---

### `gstAmount`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `totalWithoutGst`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

## Functions

### `moveItems`

**Modifiers:** override

---

### `moveOutItems`

**Modifiers:** impl

---

### `moveInItems`

**Modifiers:** impl

---

### `moveOutLE`

**Modifiers:** impl

---

### `moveOutStore`

**Modifiers:** impl

---

### `moveOutState`

**Modifiers:** impl

---

### `pathSrc`

**Modifiers:** impl

---

### `pathItems`

**Modifiers:** impl

---

### `pathCanDo`

**Returns:** `Bool`

**Modifiers:** impl

---

### `pathDst`

**Modifiers:** impl

---

### `moveInDate`

**Modifiers:** impl

---

### `moveInState`

**Modifiers:** impl

---

### `moveInStore`

**Modifiers:** impl

---

### `moveInLE`

**Modifiers:** impl

---

### `journalDate`

**Modifiers:** impl

---

### `itemOrder`

**Modifiers:** override

---

### `title`

**Modifiers:** impl

---

### `entityNumbers`

**Modifiers:** override

---

### `nextN`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

## Views

### `ref`

**Modifiers:** impl

---

### `dash`

**Modifiers:** impl

---

### `dashOut`

**Modifiers:** impl

---

### `dashIn`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

### `stateView`

---

