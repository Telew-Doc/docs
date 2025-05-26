# IIProdMoveItemOut

**Type:** interface  
**App:** flow2b.inv.move

**Extends:** [`IProdMoveItem`](../flow2b_inv_move/IProdMoveItem.md)

## Fields

### `isAwaiting`

**Type:** `Unknown`

**Modifiers:** compute

---

### `isUnav`

**Type:** `Unknown`

**Modifiers:** compute

---

### `isUnavProdItems`

**Type:** `Bool`

**Modifiers:** compute

---

### `availableStock`

**Type:** `Stock?`

**Modifiers:** compute

---

### `availableIn`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `prodMoveOut`

**Returns:** `IProdMoveOut`

---

### `moveOutPriorityDate`

**Returns:** `Date`

---

### `moveOutStockType`

**Returns:** `StockType`

---

### `outStocks`

**Returns:** `[ProdReg]?`

---

### `outStockItems`

**Returns:** `[ProdItemReg]?`

---

### `prodMove`

**Returns:** `IProdMove`

**Modifiers:** impl

---

### `needProductItems`

**Returns:** `Bool`

**Modifiers:** impl

---

### `isAv`

**Returns:** `Bool`

---

### `isAv`

---

### `isAvProdItems`

---

### `awaitingForDate`

---

### `calcAv`

---

### `calcedAv`

---

### `avPeriods`

---

### `stockDesc`

---

### `makeOutStocks`

**Returns:** `[ProdReg]?`

---

### `makeOutStockItems`

**Returns:** `[ProdItemReg]?`

---

### `outStock`

**Returns:** `ProdReg?`

---

### `createTransfer`

**Returns:** `Future[Transfer]`

---

## Views

### `availableView`

---

