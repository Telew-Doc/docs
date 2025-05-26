# DeveloperProject

**Type:** entity  
**App:** tlayen.devmarketplace

**Extends:** [`ProjectIssue`](../tlayen_devmarketplace/ProjectIssue.md)

## Fields

### `description`

**Type:** `Text`

---

### `owner`

**Type:** `User`

**Modifiers:** ref

---

### `developerRole`

**Type:** `DeveloperRole by projects`

**Modifiers:** ref

---

### `proposals`

**Type:** `[Proposal]? by project`

**Modifiers:** ref

---

### `_devsRejected`

**Type:** `[User]?`

**Modifiers:** ref

---

## Views

### `form`

**Modifiers:** impl

---

### `dash`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

