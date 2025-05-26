# BullionDealsPricing

**Type:** entity  
**App:** goldsystems.bp

**Extends:** [`IDynamicPriceModel`](../flow2b_product/IDynamicPriceModel.md)

**Implements:** `ScheduledJob`

## Fields

### `xau`

**Type:** `UMoney[NZD, 5]?`

**Modifiers:** system

---

### `xag`

**Type:** `UMoney[NZD, 5]?`

**Modifiers:** system

---

### `xpt`

**Type:** `UMoney[NZD, 5]?`

**Modifiers:** system

---

### `margins`

**Type:** `[MetalMargin]`

---

### `clearanceItems`

**Type:** `[BullionDealsClearanceItem]? inline by model`

---

## Functions

### `title`

**Modifiers:** impl

---

### `schedule`

**Modifiers:** impl

---

### `do`

**Modifiers:** override

---

### `doContains`

**Returns:** `Bool`

**Modifiers:** impl

---

### `doPrice`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

