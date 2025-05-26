# RentDeliveryItem

**Type:** entity  
**App:** flow2b.asset.fixed.rent

**Modifiers:** inline

**Extends:** [`IDlvProgressItem`](../flow2b_inv_order/IDlvProgressItem.md)

**Implements:** `FProductItems`

## Fields

### `priceModel`

**Type:** `Unknown`

**Modifiers:** compute

---

### `productPrice`

**Type:** `Unknown`

**Modifiers:** compute

---

### `unsafePeriods`

**Type:** `[Period]?`

**Modifiers:** compute

---

### `period`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `storeRequired`

**Modifiers:** override

---

### `isRent`

**Modifiers:** override

---

### `calcAv`

**Modifiers:** override

---

### `moveInStockType`

**Modifiers:** impl

---

### `moveOutStockType`

**Modifiers:** impl

---

### `needsRevision`

**Modifiers:** impl

---

### `sameAsPrev`

**Returns:** `Bool`

**Modifiers:** impl

---

### `unit`

**Returns:** `ProductUnit`

**Modifiers:** impl

---

### `priceQty`

---

### `durUpdated`

**Returns:** `Future[Void]`

---

### `toDuration`

---

### `awaitingForDate`

**Modifiers:** override

---

## Views

### `form`

**Modifiers:** impl

---

### `rowView`

**Modifiers:** impl

---

