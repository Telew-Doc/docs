# QrVersion

**Type:** entity  
**App:** flow2b.que

**Extends:** [`HasNumber`](../core/HasNumber.md)

## Fields

### `template`

**Type:** `QrTemplate`

**Modifiers:** ref

---

### `fontStyle`

**Type:** `FontStyle`

**Modifiers:** ref

---

### `name`

**Type:** `String`

---

### `question`

**Type:** `String?`

---

### `n`

**Type:** `Dec`

**Modifiers:** ref

---

### `questions`

**Type:** `[IQue]? inline by version`

---

### `params`

**Type:** `[QrVersionParam]? inline by version`

---

### `blocks`

**Type:** `[IQueBlock]? read by blockVersion`

---

### `usedIn`

**Type:** `[QrVersion]?`

**Modifiers:** compute

---

## Functions

### `number`

**Modifiers:** impl

---

### `prevVersion`

---

### `title`

**Modifiers:** impl

---

### `propagate`

**Returns:** `Bool`

**Modifiers:** back

---

### `isLast`

**Returns:** `Bool`

---

### `isUsed`

**Modifiers:** back

---

### `clone`

**Modifiers:** back

---

### `makeNewVersion`

**Returns:** `QrVersion`

**Modifiers:** back

---

## Views

### `form`

**Modifiers:** impl

---

