# Incident

**Type:** entity  
**App:** flow2b.net.dev

**Extends:** [`Issue`](../flow2b_net_sales/Issue.md)

**Implements:** `DeferredJob`

## Fields

### `unrespondedTime`

**Type:** `Duration?`

**Modifiers:** compute

---

### `preFailedStatus`

**Type:** `IssueStatus?`

**Modifiers:** system

---

### `support`

**Type:** `User?`

**Modifiers:** ref

---

### `urls`

**Type:** `[Url]?`

---

### `urgencyReason`

**Type:** `Text?`

---

### `urgency`

**Type:** `Urgency`

**Modifiers:** ref

---

### `subject`

**Type:** `String?`

**Modifiers:** ref

---

### `desc`

**Type:** `Text?`

---

## Functions

### `service`

**Modifiers:** impl

---

### `jobDate`

**Modifiers:** impl

---

### `requireEfforts`

**Modifiers:** impl

---

### `timeColor`

**Returns:** `String`

---

### `issueTypes`

**Modifiers:** override

---

### `do`

**Modifiers:** impl

---

### `statuses`

**Modifiers:** override

---

### `defaultStatus`

**Modifiers:** override

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

### `type`

**Returns:** `DevIssueType`

**Modifiers:** impl

---

### `descUpdated`

**Modifiers:** impl

---

### `spawnNewIncident`

**Returns:** `Incident`

**Modifiers:** back

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

