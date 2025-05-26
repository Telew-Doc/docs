# Milestone

**Type:** entity  
**App:** flow2b.net.dev

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `Blockable`

## Fields

### `name`

**Type:** `String`

**Modifiers:** ref

---

### `status`

**Type:** `MilestoneStatus`

**Modifiers:** ref

---

### `releaseDate`

**Type:** `Date?`

---

### `effort`

**Type:** `Unknown`

**Modifiers:** compute

---

### `description`

**Type:** `Text?`

---

### `todo`

**Type:** `[Issue]?`

**Modifiers:** compute

---

### `otherIssues`

**Type:** `[Issue]?`

**Modifiers:** compute

---

### `milestoneIssues`

**Type:** `[Issue]? read by milestone`

---

## Functions

### `title`

**Modifiers:** impl

---

### `itemRoles`

**Modifiers:** impl

---

### `canRead`

**Modifiers:** impl

---

### `isBlocking`

**Returns:** `Bool`

**Modifiers:** override

---

### `remainingEffort`

---

### `contentIssues`

**Returns:** `[Issue]?`

**Modifiers:** impl

---

### `wholeEffort`

---

### `currentNumber`

**Returns:** `UInt`

---

### `allDesireRank`

---

### `active`

**Returns:** `Bool`

**Modifiers:** impl

---

### `isInBacklog`

**Returns:** `Bool`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

