# Actor

**Type:** trait  
**App:** core

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `Addressee with HasN`

## Fields

### `desc`

**Type:** `Text?`

---

### `actorWorkspaceId`

**Type:** `UInt?`

---

### `currency`

**Type:** `Currency?`

**Modifiers:** ref

---

### `people`

**Type:** `[CompanyPerson]? inline by company`

---

## Functions

### `our`

**Returns:** `OurActor?`

---

### `nextN`

**Modifiers:** impl

---

### `current`

**Returns:** `Actor?`

**Modifiers:** native, object

---

### `addresseeCompany`

**Returns:** `Actor?`

**Modifiers:** impl

---

### `isTheir`

**Returns:** `Bool`

---

### `getCurrency`

---

### `top`

**Returns:** `Actor`

---

### `isTop`

**Returns:** `Bool`

---

### `isLegalCompany`

**Returns:** `Bool`

---

### `legalEntities`

**Returns:** `[LegalEntity]`

---

### `all`

**Returns:** `[Actor]`

---

### `shortForm`

**Returns:** `Layout[Actor]`

---

### `addPerson`

**Returns:** `CompanyPerson?`

**Modifiers:** back

---

