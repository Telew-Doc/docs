# Feature

**Type:** entity  
**App:** flow2b.net.dev

## Fields

### `number`

**Type:** `String`

**Modifiers:** compute

---

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `roadmap`

**Type:** `Roadmap`

**Modifiers:** ref

---

### `status`

**Type:** `FeatureStatus`

**Modifiers:** ref

---

### `products`

**Type:** `[DevProduct]`

---

### `effort`

**Type:** `Effort?`

**Modifiers:** ref

---

### `stories`

**Type:** `[BacklogIssue]? read by feature`

---

### `role`

**Type:** `ProductRole`

---

### `goal`

**Type:** `Text`

---

### `benefit`

**Type:** `Text`

---

### `additionalInfo`

**Type:** `Text?`

---

## Functions

### `title`

**Modifiers:** impl

---

### `canRead`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

