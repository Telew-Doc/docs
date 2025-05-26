# Ledger

**Type:** trait  
**App:** flow2b.acc.base

**Modifiers:** inline

**Extends:** [`Register`](../core/Register.md)

**Implements:** `HasDate`

## Fields

### `journal`

**Type:** `Journal`

---

### `contraAccount`

**Type:** `LedgerAccount?`

---

### `trAmount`

**Type:** `Money[currency]?`

---

### `subAccount`

**Type:** `LedgerSubAccount`

**Modifiers:** compute

---

### `debit`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `credit`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `debitBalance`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `creditBalance`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

## Functions

### `aview`

**Returns:** `Layout[Ledger]`

---

### `currency`

**Returns:** `Currency`

---

### `account`

**Returns:** `LedgerAccount`

---

### `isCorrection`

---

### `isClosing`

---

### `makeContra`

**Returns:** `Void`

---

### `taxableAmount`

**Returns:** `Money[currency]?`

---

### `subBalances`

---

### `createIncomeSummary`

---

### `mlBalance`

**Returns:** `MLedger`

---

