# ProdReg

**Type:** register  
**App:** flow2b.inv.stock

## Fields

### `doc`

**Type:** `RefEntity`

---

### `docItem`

**Type:** `AnyEntity? inline`

---

### `productItems`

**Type:** `[IProductItem]?`

---

### `isFact`

**Type:** `Bool`

**Modifiers:** compute

---

### `isRent`

**Type:** `Bool`

---

### `isStocktake`

**Type:** `Bool`

---

### `qty`

**Type:** `Qty[unit]?`

---

### `factualQty`

**Type:** `Qty[unit]?`

**Modifiers:** compute

---

### `reservedQty`

**Type:** `Qty[unit]?`

**Modifiers:** compute

---

### `expectedQty`

**Type:** `Qty[unit]?`

**Modifiers:** compute

---

### `quotedQty`

**Type:** `Qty[unit]?`

**Modifiers:** compute

---

### `factualChange`

**Type:** `Qty[unit]?`

**Modifiers:** compute

---

### `available`

**Type:** `Qty[unit]?`

**Modifiers:** compute

---

### `outlook`

**Type:** `Qty[unit]?`

**Modifiers:** compute

---

### `stocktakeCost`

**Type:** `Money[legalEntity.getCurrency]?`

---

### `awaitingForDate`

**Type:** `Date?`

**Modifiers:** compute

---

## Functions

### `unit`

---

### `isReserve`

---

### `apply`

**Returns:** `Qty[unit]?`

---

### `isAv`

**Returns:** `Bool`

---

### `isEmpty`

---

### `prevStock`

**Returns:** `Stock`

---

### `stock`

**Returns:** `Stock`

---

### `stockStore`

**Returns:** `StockStore`

---

### `prevStockStore`

---

### `availableQtyPeriods`

**Returns:** `[QtyPeriod]`

---

### `avPeriods`

**Returns:** `[Period]?`

---

### `availabilitySwitchDates`

**Returns:** `[Date]?`

---

