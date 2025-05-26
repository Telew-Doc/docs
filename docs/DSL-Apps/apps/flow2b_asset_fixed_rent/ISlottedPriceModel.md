# ISlottedPriceModel

**Type:** trait  
**App:** flow2b.asset.fixed.rent

**Extends:** [`IPriceModel`](../flow2b_product/IPriceModel.md)

## Fields

### `cycle`

**Type:** `UDuration[minute]`

**Modifiers:** compute

---

## Functions

### `isSalesModel`

**Modifiers:** impl

---

### `isRentModel`

**Modifiers:** impl

---

### `hasSlots`

**Modifiers:** impl

---

### `period`

**Returns:** `Period`

---

### `durations`

**Returns:** `[DurationSlot]`

---

### `slots`

**Returns:** `[RentSlot]`

---

### `pricesIncludingGst`

**Returns:** `Bool`

---

### `allDurUnits`

**Returns:** `[DurUnit]?`

**Modifiers:** impl

---

### `validateSlots`

**Returns:** `String?`

---

### `slots`

**Returns:** `[RentSlot]?`

---

### `toSlotsCount`

**Returns:** `UQty[Slot]?`

---

### `slotsCount`

**Returns:** `UQty[Slot]?`

---

### `rentPeriods`

**Returns:** `[Period]?`

---

