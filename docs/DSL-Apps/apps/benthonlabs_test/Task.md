# Task

**Type:** entity  
**App:** benthonlabs.test

## Fields

### `description`

**Type:** `Text?`

---

### `taskClassType`

**Type:** `TaskClassType?`

---

### `createdBy`

**Type:** `Person?`

**Modifiers:** ref

---

### `assigned_to`

**Type:** `Person?`

---

### `created_at`

**Type:** `Date`

---

### `status`

**Type:** `TaskStatus?`

---

### `task_list_type`

**Type:** `TaskListType?`

---

### `task_type`

**Type:** `TaskType?`

---

### `sub_tasks`

**Type:** `[Task]?`

---

### `project`

**Type:** `Project?`

---

### `totalTime`

**Type:** `UDuration?`

---

### `required_time`

**Type:** `UDuration?`

---

### `comments`

**Type:** `[Comment]?`

---

### `timelogs`

**Type:** `[TimeLog]?`

---

### `changelists`

**Type:** `[ChangeList]?`

---

### `users`

**Type:** `[Person]?`

---

## Functions

### `update_total_time`

---

## Views

### `form`

**Modifiers:** impl

---

