# Stocktake

**Type:** entity  
**App:** flow2b.inv.move

**Extends:** [`StockCorrection`](../flow2b_inv_move/StockCorrection.md)

## Fields

### `stockType`

**Type:** `StockInvType`

**Modifiers:** ref

---

### `type`

**Type:** `StocktakeType`

---

### `items`

**Type:** `[StocktakeItem]? inline by stocktake`

---

## Functions

### `assetProducts`

**Returns:** `[IProductInv: UQty]?`

---

### `number`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `fillWithCurrentStock`

**Returns:** `Future[Void]`

**Modifiers:** back

---

### `addMissingItems`

**Returns:** `Future[Void]`

---

### `procBarcode`

**Returns:** `Future[Void]`

**Modifiers:** front

---

### `procNfc`

**Returns:** `Future[Void]`

**Modifiers:** front

---

### `addQty`

**Returns:** `StocktakeItem`

---

## Views

### `ref`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

