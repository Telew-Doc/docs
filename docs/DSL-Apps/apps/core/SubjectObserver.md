# SubjectObserver

**Type:** entity  
**App:** core

**Modifiers:** inline

## Fields

### `subject`

**Type:** `Entity by observers`

---

### `observer`

**Type:** `IContact by subjects`

---

### `issues`

**Type:** `[IssueType[Entity]]? by issueObservers`

---

### `unreadCount`

**Type:** `Int?`

---

### `pinned`

**Type:** `Bool`

---

### `active`

**Type:** `Bool`

---

### `fullUnreadCount`

**Type:** `Unknown`

**Modifiers:** compute

---

### `panelUnreadCount`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `is`

**Returns:** `Bool`

---

### `_is`

**Returns:** `Bool`

**Modifiers:** back

---

### `subjectType`

---

### `badgeUnreadCount`

**Returns:** `Int?`

---

### `_badgeUnreadCount`

**Returns:** `Int?`

**Modifiers:** back

---

### `pin`

**Returns:** `SubjectObserver`

---

### `notify`

**Returns:** `SubjectObserver`

---

### `toString`

**Modifiers:** impl

---

