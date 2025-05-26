# PersonalProject

**Type:** entity  
**App:** flow2b.net.dev

**Extends:** [`DevProduct`](../flow2b_net_dev/DevProduct.md)

## Fields

### `name`

**Type:** `String?`

**Modifiers:** ref

---

### `actor`

**Type:** `Actor by projects`

**Modifiers:** ref

---

### `questionnaires`

**Type:** `[Questionnaire]?`

**Modifiers:** compute

---

### `issuesByMilestone`

**Type:** `[(milestone: Milestone?, blockStatus: BlockStatus?, isBlocked: Bool, issues: [Issue]?)]`

**Modifiers:** compute

---

### `unresolvedIncidents`

**Type:** `[Incident]?`

**Modifiers:** compute

---

### `insidentsBlocked`

**Type:** `[Issue]?`

**Modifiers:** compute

---

## Functions

### `isTangible`

---

### `title`

**Modifiers:** impl

---

### `type`

**Returns:** `ProductType`

**Modifiers:** impl

---

### `subProducts`

---

### `isTheir`

---

### `canRead`

**Returns:** `Bool`

**Modifiers:** impl

---

### `canWrite`

**Returns:** `Bool`

**Modifiers:** impl

---

### `multiupdate`

**Modifiers:** impl

---

## Views

### `ref`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

