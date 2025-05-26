# Backlog

**Type:** entity  
**App:** flow2b.net.dev

## Fields

### `active`

**Type:** `Bool`

---

### `devType`

**Type:** `DevType`

---

### `name`

**Type:** `String?`

**Modifiers:** ref

---

### `products`

**Type:** `[DevProduct]? by backlog`

---

### `allIssues`

**Type:** `[BacklogIssue]? read by backlog`

**Modifiers:** system

---

### `verifiedIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `qaIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `progressIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `todoIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `backlogIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `estimateIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `heapIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `enteredIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `qaReviewIssues`

**Type:** `Unknown`

**Modifiers:** compute

---

### `backlogLimit`

**Type:** `UInt`

---

### `heapLimit`

**Type:** `UInt`

---

### `enteredLimit`

**Type:** `UInt`

---

### `devLimit`

**Type:** `UInt`

---

### `qaLimit`

**Type:** `UInt`

---

### `backlogSize`

**Type:** `UInt?`

**Modifiers:** compute

---

### `heapSize`

**Type:** `UInt?`

**Modifiers:** compute

---

### `enteredSize`

**Type:** `UInt?`

**Modifiers:** compute

---

### `devSize`

**Type:** `UInt?`

**Modifiers:** compute

---

### `qaSize`

**Type:** `UInt?`

**Modifiers:** compute

---

## Functions

### `itemRoles`

**Modifiers:** impl

---

### `issueTypes`

**Modifiers:** override

---

### `canRead`

**Modifiers:** impl

---

## Views

### `backlogView`

---

### `form`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

