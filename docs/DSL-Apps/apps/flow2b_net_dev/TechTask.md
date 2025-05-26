# TechTask

**Type:** entity  
**App:** flow2b.net.dev

**Extends:** [`Issue`](../flow2b_net_sales/Issue.md)

## Fields

### `taskType`

**Type:** `TechTaskType`

**Modifiers:** ref

---

### `name`

**Type:** `String?`

**Modifiers:** ref

---

### `tech`

**Type:** `User?`

**Modifiers:** ref

---

### `params`

**Type:** `[ParamValue]? inline by tech`

---

### `urgency`

**Type:** `Urgency`

**Modifiers:** ref

---

### `desc`

**Type:** `Text?`

---

### `howTo`

**Type:** `Text?`

**Modifiers:** compute

---

## Functions

### `stdCharge`

**Returns:** `UMoney[our]?`

**Modifiers:** impl

---

### `developer`

**Modifiers:** impl

---

### `isBlocking`

**Returns:** `Bool`

**Modifiers:** override

---

### `numPrefix`

**Returns:** `String`

**Modifiers:** impl

---

### `additionalDesire`

**Modifiers:** impl

---

### `itemRoles`

**Modifiers:** impl

---

### `issueTypes`

**Modifiers:** override

---

### `type`

**Returns:** `DevIssueType`

**Modifiers:** impl

---

### `descUpdated`

**Modifiers:** impl

---

## Views

### `ref`

**Modifiers:** impl

---

### `traitItem`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

