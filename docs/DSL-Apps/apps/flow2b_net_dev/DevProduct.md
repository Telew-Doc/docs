# DevProduct

**Type:** trait  
**App:** flow2b.net.dev

**Extends:** [`RefEntity`](../core/RefEntity.md)

## Fields

### `files`

**Type:** `[File]?`

---

### `description`

**Type:** `Text?`

---

### `status`

**Type:** `ProductStatus`

---

### `sandboxWorkspace`

**Type:** `String?`

---

### `milestones`

**Type:** `[Milestone]? read by products`

**Modifiers:** ref

---

### `features`

**Type:** `[Feature]? read by products`

**Modifiers:** ref

---

### `docs`

**Type:** `[Article]? from Article.all.filter`

---

### `packageDocs`

**Type:** `[DocPackage]? by product`

---

### `backlog`

**Type:** `Backlog? by products`

**Modifiers:** ref

---

### `dependencies`

**Type:** `[UniversalApp]? by dependants`

---

### `roadmap`

**Type:** `Roadmap? by products`

**Modifiers:** ref

---

### `devIssues`

**Type:** `[Issue]? read by _product`

**Modifiers:** system

---

## Functions

### `type`

**Returns:** `ProductType`

---

### `devType`

**Returns:** `DevType`

---

### `supportUnits`

**Returns:** `Int?`

---

### `milestonesSelection`

---

### `rank`

**Returns:** `UDec[2]`

---

### `allDependants`

**Returns:** `[DevProduct]?`

---

### `openIssues`

**Modifiers:** front

---

