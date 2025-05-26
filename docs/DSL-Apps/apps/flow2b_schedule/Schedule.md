# Schedule

**Type:** entity  
**App:** flow2b.schedule

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `ISchedule`

## Fields

### `workingHoursPerDay`

**Type:** `UDuration[hour]`

---

### `cycle`

**Type:** `UDuration[day]`

**Modifiers:** compute

---

### `period`

**Type:** `Period`

---

### `workingPeriods`

**Type:** `[Period]`

---

### `exceptions`

**Type:** `[Exception]?`

---

## Functions

### `correctForward`

**Returns:** `Period?`

**Modifiers:** impl

---

### `workingPeriod`

**Returns:** `Period?`

**Modifiers:** impl

---

### `delta`

**Returns:** `Duration[day]?`

---

### `prevPeriod`

**Returns:** `Period?`

**Modifiers:** impl

---

### `nextPeriod`

**Returns:** `Period?`

**Modifiers:** impl

---

### `isWorkingPeriod`

**Returns:** `Bool`

**Modifiers:** impl

---

### `isWorkingDate`

**Returns:** `Bool`

**Modifiers:** impl

---

### `nextWorkingDate`

**Returns:** `Date?`

**Modifiers:** impl

---

### `prevWorkingDate`

**Returns:** `Date?`

**Modifiers:** impl

---

### `addWorkingTime`

**Returns:** `Date?`

**Modifiers:** impl

---

### `workingTime`

**Returns:** `UDuration?`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

