# Person

**Type:** entity  
**App:** core

**Extends:** [`LegalEntity`](../flow2b_payment/LegalEntity.md)

## Fields

### `photos`

**Type:** `[Image]?`

---

### `gender`

**Type:** `Gender?`

---

### `user`

**Type:** `User? inline by person`

**Modifiers:** ref

---

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `companies`

**Type:** `[CompanyPerson]? inline by person`

---

### `birthdate`

**Type:** `UtcDate[day]?`

---

### `companyPerson`

**Type:** `CompanyPerson`

**Modifiers:** compute

---

### `company`

**Type:** `Actor?`

**Modifiers:** compute

---

## Functions

### `numPrefix`

**Modifiers:** impl

---

### `isOur`

**Modifiers:** impl

---

### `addresseePerson`

**Returns:** `Person?`

**Modifiers:** impl

---

### `collectContacts`

**Returns:** `[ActorContact]?`

**Modifiers:** impl

---

### `firstName`

**Returns:** `String`

---

### `current`

**Returns:** `Person?`

**Modifiers:** native, object

---

### `systemContact`

**Returns:** `Contact?`

**Modifiers:** impl

---

### `isCurrent`

---

### `isTheir`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

### `shortForm`

**Modifiers:** impl

---

### `quick`

**Modifiers:** impl

---

