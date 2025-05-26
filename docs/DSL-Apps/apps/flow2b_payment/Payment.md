# Payment

**Type:** trait  
**App:** flow2b.payment

**Extends:** [`CashMovement`](../tubularequipment_wf/CashMovement.md)

**Implements:** `DebtOrigin with IReasonOwner`

## Fields

### `source`

**Type:** `PaymentSource?`

---

### `desc`

**Type:** `Text?`

---

### `amount`

**Type:** `UMoney[currency]`

**Modifiers:** ref

---

### `mAmount`

**Type:** `Money[currency]`

**Modifiers:** compute

---

### `bankData`

**Type:** `BankData`

---

### `recRefs`

**Type:** `[RefEntity]?`

**Modifiers:** compute

---

### `accountAmount`

**Type:** `UMoney[account.currency]?`

---

### `accountAmountEditor`

**Type:** `UMoney[account.currency]`

**Modifiers:** compute

---

## Functions

### `isInstant`

**Modifiers:** impl

---

### `number`

**Returns:** `String`

---

### `isIncoming`

**Returns:** `Bool`

---

### `journal`

**Modifiers:** impl

---

### `noCpTitle`

**Modifiers:** impl

---

### `allManLinks`

**Returns:** `[DebtOrigin]?`

**Modifiers:** override

---

### `hasSource`

**Returns:** `Bool`

**Modifiers:** impl

---

### `movedAmount`

**Returns:** `Money[currency]`

---

### `debtCurrency`

**Modifiers:** impl

---

### `validateReasons`

**Modifiers:** impl

---

### `moneyCalced`

**Returns:** `Bool`

**Modifiers:** back

---

### `isMissingInBSU`

**Modifiers:** impl

---

### `issueTypes`

**Modifiers:** override

---

### `merge`

**Returns:** `Payment`

**Modifiers:** back

---

### `cpName`

**Returns:** `String`

---

### `debtDueDate`

**Returns:** `Date?`

---

### `origin`

---

### `amountUpdated`

**Returns:** `Void`

---

### `paidAmount`

---

### `paymentCashFlows`

**Modifiers:** override

---

