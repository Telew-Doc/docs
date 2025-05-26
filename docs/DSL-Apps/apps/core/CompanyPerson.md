# CompanyPerson

**Type:** entity  
**App:** core

**Extends:** [`PseudoEntity`](../core/PseudoEntity.md)

**Implements:** `Addressee`

## Fields

### `company`

**Type:** `Actor by people`

**Modifiers:** ref

---

### `person`

**Type:** `Person by companies`

**Modifiers:** ref

---

### `desc`

**Type:** `Text?`

---

### `jobTitle`

**Type:** `JobTitle? by people`

---

## Functions

### `mainEntity`

**Modifiers:** impl

---

### `isOur`

**Modifiers:** impl

---

### `addresseePerson`

**Returns:** `Person?`

**Modifiers:** impl

---

### `addresseeCompany`

**Returns:** `Actor?`

**Modifiers:** impl

---

### `systemContact`

**Returns:** `Contact?`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

## Views

### `shortForm`

---

### `form`

**Modifiers:** impl

---

### `quick`

**Modifiers:** impl

---

### `stateView`

---

