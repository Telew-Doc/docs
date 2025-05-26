# AppVersion

**Type:** entity  
**App:** core

## Fields

### `app`

**Type:** `App by versions`

**Modifiers:** ref

---

### `version`

**Type:** `String`

**Modifiers:** ref

---

### `status`

**Type:** `AppVersionStatus`

**Modifiers:** ref

---

### `releaseNotes`

**Type:** `Text?`

---

### `files`

**Type:** `[AppFile]?`

---

### `dependencies`

**Type:** `[Dependency]?`

---

### `readOnly`

**Type:** `Bool`

---

### `errors`

**Type:** `[Error]?`

---

## Functions

### `title`

**Returns:** `String`

**Modifiers:** impl

---

### `addDependency`

**Returns:** `Void`

---

### `openIssues`

**Returns:** `Void`

**Modifiers:** front

---

### `dependencyVersions`

**Returns:** `Future[[AppVersion]?]`

**Modifiers:** back

---

### `allDependencyVersions`

**Returns:** `Future[[AppVersion]]`

**Modifiers:** back

---

### `unload`

---

## Views

### `ref`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

