# ProductRole

**Type:** entity  
**App:** flow2b.net.dev

## Fields

### `status`

**Type:** `RoleStatus`

---

### `superRoles`

**Type:** `[ProductRole]? by subRoles`

---

### `subRoles`

**Type:** `[ProductRole]? read by superRoles`

---

### `description`

**Type:** `Text?`

---

### `features`

**Type:** `[Feature]? read by role`

---

### `stories`

**Type:** `[IUserStory]? read by role`

---

## Functions

### `itemRoles`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

