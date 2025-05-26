# BullionDealsClearanceItem

**Type:** entity  
**App:** goldsystems.bp

**Modifiers:** inline

**Extends:** [`IMetalMargin`](../goldsystems_bp/IMetalMargin.md)

## Fields

### `model`

**Type:** `BullionDealsPricing by clearanceItems`

**Modifiers:** system

---

### `product`

**Type:** `BullionSuperProduct`

---

### `originalMaxMargin`

**Type:** `Future[Percent[2]?]`

**Modifiers:** compute

---

### `originalMaxPrice`

**Type:** `Future[UMoney?]`

**Modifiers:** compute

---

### `newMaxPrice`

**Type:** `Future[UMoney?]`

**Modifiers:** compute

---

### `origMaxMarginPrice`

**Type:** `Future[OrigPrice]`

**Modifiers:** compute

---

### `originalMinMargin`

**Type:** `Future[Percent[2]?]`

**Modifiers:** compute

---

### `originalMinPrice`

**Type:** `Future[UMoney?]`

**Modifiers:** compute

---

### `newMinPrice`

**Type:** `Future[UMoney?]`

**Modifiers:** compute

---

### `origMinMarginPrice`

**Type:** `Future[OrigPrice]`

**Modifiers:** compute

---

## Functions

### `unit`

**Modifiers:** impl

---

### `originalMargin`

**Returns:** `Future[OrigPrice]`

---

