# OrderTerms

**Type:** entity  
**App:** flow2b.invoice

**Extends:** [`IOrderTerms`](../flow2b_invoice/IOrderTerms.md)

## Fields

### `priceGst`

**Type:** `TermsGst`

**Modifiers:** ref

---

### `acceptance`

**Type:** `OTAcceptance?`

**Modifiers:** ref

---

### `prepayment`

**Type:** `OTPrepayment?`

**Modifiers:** ref

---

### `predelivery`

**Type:** `OTPredelivery?`

**Modifiers:** ref

---

### `delivery`

**Type:** `OTDelivery?`

**Modifiers:** ref

---

### `postdelivery`

**Type:** `OTPostdelivery?`

**Modifiers:** ref

---

## Functions

### `prePercent`

---

### `dispatchDate`

**Returns:** `Date?`

**Modifiers:** impl

---

### `canDispatch`

**Modifiers:** override

---

### `inclGst`

**Returns:** `Bool`

**Modifiers:** impl

---

### `due`

**Returns:** `Due`

**Modifiers:** impl

---

### `orderState`

**Returns:** `OrderState`

**Modifiers:** impl

---

### `hasAcceptance`

**Returns:** `Bool`

**Modifiers:** impl

---

### `toDispatchState`

**Returns:** `OrderState`

---

### `updatableStates`

**Returns:** `[OrderState]`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

