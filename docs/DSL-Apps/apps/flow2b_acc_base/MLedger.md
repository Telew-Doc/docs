# MLedger

**Type:** trait  
**App:** flow2b.acc.base

**Extends:** [`InlineEntity`](../core/InlineEntity.md)

## Fields

### `journal`

**Type:** `MJournal by entries`

---

### `account`

**Type:** `LedgerAccount`

**Modifiers:** ref

---

### `subAccount`

**Type:** `LedgerSubAccount?`

---

### `isDebit`

**Type:** `Bool`

---

### `contraAccount`

**Type:** `LedgerAccount?`

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

### `accountEditor`

**Type:** `LedgerSubAccount`

**Modifiers:** compute

---

### `amount`

**Type:** `Money[currency]?`

**Modifiers:** ref

---

### `cor`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `legalEntity`

**Returns:** `OurLegalEntity`

---

### `currency`

**Returns:** `Currency`

---

### `needLedger`

**Returns:** `Bool`

---

### `calculatedAmount`

**Returns:** `Bool`

---

### `syncAnalit`

**Returns:** `Void`

---

### `aview`

**Returns:** `Layout`

---

### `debitEditor`

**Returns:** `Layout`

---

### `creditEditor`

**Returns:** `Layout`

---

## Views

### `creditView`

---

### `debitView`

---

