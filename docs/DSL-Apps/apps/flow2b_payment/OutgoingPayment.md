# OutgoingPayment

**Type:** entity  
**App:** flow2b.payment

**Extends:** [`Payment`](../flow2b_payment/Payment.md)

**Implements:** `OPReasonOwner`

## Fields

### `payer`

**Type:** `OurLegalEntity`

**Modifiers:** ref

---

## Functions

### `legalEntity`

**Modifiers:** impl

---

### `srcAccount`

**Returns:** `FinAccount?`

**Modifiers:** impl

---

### `dstAccount`

**Returns:** `FinAccount?`

**Modifiers:** impl

---

### `debtAmount`

**Modifiers:** impl

---

### `movedAmount`

**Returns:** `Money[currency]`

**Modifiers:** impl

---

### `debtCashFlows`

**Modifiers:** impl

---

### `cpName`

**Returns:** `String`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `defaultReasons`

**Modifiers:** impl

---

### `defaultRecon`

**Returns:** `OPReason?`

---

### `isTheir`

---

### `isIncoming`

**Returns:** `Bool`

**Modifiers:** impl

---

### `isPurchase`

**Modifiers:** impl

---

### `converters`

**Modifiers:** impl

---

## Views

### `ref`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

### `stateView`

---

### `posViewDebit`

**Modifiers:** override

---

### `posViewCredit`

**Modifiers:** override

---

