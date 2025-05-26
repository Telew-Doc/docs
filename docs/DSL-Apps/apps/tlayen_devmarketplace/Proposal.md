# Proposal

**Type:** entity  
**App:** tlayen.devmarketplace

**Extends:** [`ProposalIssue`](../tlayen_devmarketplace/ProposalIssue.md)

## Fields

### `owner`

**Type:** `User`

**Modifiers:** ref

---

### `suitability`

**Type:** `Suitability`

---

### `details`

**Type:** `Text?`

---

### `budget`

**Type:** `Money[currency]`

---

### `currency`

**Type:** `Currency`

---

### `project`

**Type:** `DeveloperProject by proposals`

**Modifiers:** ref

---

## Views

### `form`

**Modifiers:** impl

---

