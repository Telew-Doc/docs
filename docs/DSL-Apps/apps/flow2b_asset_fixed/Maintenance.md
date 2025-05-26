# Maintenance

**Type:** entity  
**App:** flow2b.asset.fixed

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `HasNumber`

## Fields

### `productItem`

**Type:** `ProductItem by maintenances`

**Modifiers:** ref

---

### `start`

**Type:** `Date`

**Modifiers:** ref

---

### `end`

**Type:** `Date?`

**Modifiers:** ref

---

### `status`

**Type:** `MaintenanceStatus`

**Modifiers:** ref

---

### `type`

**Type:** `MaintananceType?`

**Modifiers:** ref

---

### `description`

**Type:** `Text?`

---

### `nextUnit`

**Type:** `DateUnit`

---

### `nextDelta`

**Type:** `Duration[nextUnit]?`

---

### `nextMaintenance`

**Type:** `Maintenance?`

**Modifiers:** const

---

## Functions

### `number`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `itemOrder`

**Modifiers:** override

---

### `itemRoles`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

### `dash`

**Modifiers:** impl

---

