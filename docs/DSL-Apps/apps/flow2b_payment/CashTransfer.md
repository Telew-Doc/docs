# CashTransfer

**Type:** entity  
**App:** flow2b.payment

**Extends:** [`CashMovement`](../tubularequipment_wf/CashMovement.md)

## Fields

### `from`

**Type:** `FinAccount`

**Modifiers:** ref

---

### `outcome`

**Type:** `UMoney[from.currency]`

**Modifiers:** ref

---

### `to`

**Type:** `FinAccount`

**Modifiers:** ref

---

### `income`

**Type:** `UMoney[to.currency]`

**Modifiers:** ref

---

### `outgoingBankData`

**Type:** `BankData`

---

### `status`

**Type:** `CashTransferStatus`

---

### `incomingBankData`

**Type:** `BankData`

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

### `isMissingInBSU`

**Modifiers:** impl

---

### `debtCounterparty`

**Returns:** `LegalEntity?`

**Modifiers:** impl

---

### `reconState`

**Returns:** `ReconState`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `date`

**Returns:** `Date`

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

