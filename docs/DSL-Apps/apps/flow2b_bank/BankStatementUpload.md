# BankStatementUpload

**Type:** entity  
**App:** flow2b.bank

**Extends:** [`ImportTask`](../core/ImportTask.md)

## Fields

### `unknownAccount`

**Type:** `Bool`

---

### `defineAccount`

**Type:** `Bool`

---

### `type`

**Type:** `BankStatementType?`

---

### `account`

**Type:** `FinAccount?`

---

### `files`

**Type:** `[File]`

---

### `payments`

**Type:** `[CashMovement]? by uploads`

**Modifiers:** const

---

## Functions

### `service`

**Modifiers:** impl

---

### `itemRoles`

**Modifiers:** impl

---

### `issueTypes`

**Modifiers:** override

---

### `title`

**Modifiers:** override

---

### `createJob`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

### `traitItem`

**Modifiers:** impl

---

