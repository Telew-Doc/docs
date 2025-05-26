# IAmountItem

**Type:** trait  
**App:** flow2b.inv.move

**Extends:** [`InlineEntity`](../core/InlineEntity.md)

## Fields

### `sAmount`

**Type:** `UMoney[currency]?`

---

### `amountNoGst`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `amountWithGst`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `amount`

**Type:** `Unknown`

**Modifiers:** compute

---

### `amountEditor`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `gstAmount`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `totalWithGst`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `totalNoGst`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `total`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `storedWithGst`

**Type:** `Bool`

---

### `_discountUnit`

**Type:** `Unit?`

---

### `discountUnit`

**Type:** `Unit`

**Modifiers:** compute

---

### `sDiscount`

**Type:** `Number[discountUnit]?`

---

### `discountMoney`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `discountNoGst`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `discountWithGst`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `discountEditor`

**Type:** `Number[discountUnit]?`

**Modifiers:** compute

---

### `discount`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `gstRate`

**Type:** `UPercent[2]??`

---

### `gstValue`

**Type:** `UPercent[2]?`

**Modifiers:** compute

---

### `hasGst`

**Type:** `Bool`

**Modifiers:** compute

---

## Functions

### `currency`

**Returns:** `Currency`

---

### `pricesIncludingGst`

**Returns:** `Bool`

---

### `considerGst`

**Returns:** `Bool`

---

### `defaultGstRate`

**Returns:** `UPercent[2]??`

---

### `gstRateK`

---

### `validateDiscount`

---

### `total`

**Returns:** `Money[currency]?`

---

### `calcDiscount`

**Returns:** `Money[currency]?`

---

### `calcDiscountNoGst`

**Returns:** `Money[currency]?`

---

### `calcDiscountWithGst`

**Returns:** `Money[currency]?`

---

### `updateGst`

**Returns:** `Void`

---

## Views

### `gstEditor`

---

