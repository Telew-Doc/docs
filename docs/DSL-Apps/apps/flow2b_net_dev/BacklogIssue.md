# BacklogIssue

**Type:** trait  
**App:** flow2b.net.dev

**Extends:** [`Issue`](../flow2b_net_sales/Issue.md)

## Fields

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `epic`

**Type:** `Epic?`

---

### `feature`

**Type:** `Feature? by stories from product.features.filter(_.status.canChoose)`

**Modifiers:** ref

---

## Functions

### `issueTypes`

**Modifiers:** override

---

### `fix`

**Modifiers:** back

---

