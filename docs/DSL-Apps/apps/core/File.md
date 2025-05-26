# File

**Type:** trait  
**App:** core

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `HasN`

## Fields

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `sTitle`

**Type:** `String?`

**Modifiers:** ref

---

### `description`

**Type:** `Text?`

---

### `kbs`

**Type:** `String`

**Modifiers:** compute

---

### `content`

**Type:** `Future[Data?]`

**Modifiers:** compute

---

### `uploadUrl`

**Type:** `Url?`

**Modifiers:** compute

---

### `_sourceUrl`

**Type:** `Url?`

---

### `self`

**Type:** `File`

**Modifiers:** compute

---

## Functions

### `searchStr`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `nextN`

**Modifiers:** impl

---

### `plainText`

**Modifiers:** back

---

### `extension`

**Returns:** `String?`

**Modifiers:** object

---

### `obj`

**Returns:** `File.object`

**Modifiers:** object

---

### `fileName`

**Returns:** `String`

**Modifiers:** object

---

### `getContent`

**Returns:** `Future[Data?]`

**Modifiers:** native

---

### `setContent`

**Returns:** `Void`

**Modifiers:** native

---

### `getUrl`

**Returns:** `Url?`

**Modifiers:** native

---

### `getUploadUrl`

**Returns:** `Url?`

**Modifiers:** native

---

### `extension`

---

### `is`

**Returns:** `Bool`

---

