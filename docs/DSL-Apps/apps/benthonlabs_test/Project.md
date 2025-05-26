# Project

**Type:** entity  
**App:** benthonlabs.test

## Fields

### `description`

**Type:** `String?`

**Modifiers:** ref

---

### `createdBy`

**Type:** `Person?`

---

### `createdAt`

**Type:** `Date?`

---

### `assigned_to`

**Type:** `Person?`

---

### `status`

**Type:** `TaskStatus?`

---

### `taskType`

**Type:** `TaskType?`

---

### `users`

**Type:** `[Person]?`

---

### `totalTime`

**Type:** `UDuration?`

**Modifiers:** ref

---

### `required_time`

**Type:** `UDuration?`

---

### `comments`

**Type:** `[Comment]?`

---

### `tasks`

**Type:** `[Task]? by project`

---

## Functions

### `update_total_time`

---

## Views

### `form`

**Modifiers:** impl

---

