# IReconRule

**Type:** trait  
**App:** flow2b.bank

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

## Fields

### `ruleMovements`

**Type:** `[CashMovement]? read by rules`

---

### `movementsCount`

**Type:** `UInt?`

**Modifiers:** compute

---

### `_priority`

**Type:** `Dec[4]??`

---

### `frontDescr`

**Type:** `Unknown`

**Modifiers:** compute

---

### `state`

**Type:** `ReconRuleState`

**Modifiers:** ref

---

## Functions

### `backDescr`

**Returns:** `Text?`

**Modifiers:** back

---

### `pr`

**Returns:** `Dec[4]?`

---

### `run`

**Returns:** `CashMovement?`

**Modifiers:** back

---

### `isCounterparty`

**Returns:** `Bool`

**Modifiers:** back

---

### `run`

**Returns:** `[CashMovement]?`

**Modifiers:** back

---

### `defaultState`

**Returns:** `ReconRuleState`

---

## Views

### `ref`

**Modifiers:** impl

---

### `movementsView`

---

### `form`

**Modifiers:** impl

---

