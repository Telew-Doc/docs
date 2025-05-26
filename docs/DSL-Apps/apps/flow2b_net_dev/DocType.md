# DocType

**Type:** entity  
**App:** flow2b.net.dev

## Fields

### `package`

**Type:** `DocPackage by types`

**Modifiers:** ref

---

### `extension`

**Type:** `Bool`

**Modifiers:** ref

---

### `extensionPackage`

**Type:** `DocPackage?`

**Modifiers:** ref

---

### `type`

**Type:** `TypeType`

**Modifiers:** ref

---

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `superTypes`

**Type:** `[DocType]? by childTypes`

---

### `childTypes`

**Type:** `[DocType]? by superTypes`

---

### `description`

**Type:** `Text?`

---

### `declarations`

**Type:** `[DocDecl]? read by docType`

---

## Functions

### `fullName`

---

### `title`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

