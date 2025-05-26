# Payroll

**Type:** entity  
**App:** flow2b.net.hr

**Extends:** [`HasN`](../core/HasN.md)

## Fields

### `complete`

**Type:** `Bool`

---

### `prev`

**Type:** `Payroll?`

**Modifiers:** compute

---

### `_start`

**Type:** `Date`

**Modifiers:** ref

---

### `start`

**Type:** `Date`

**Modifiers:** compute

---

### `end`

**Type:** `Date`

**Modifiers:** compute

---

### `timetables`

**Type:** `[Timetable]? read by payroll`

---

### `totalAll`

**Type:** `Unknown`

**Modifiers:** compute

---

### `totalCustomer`

**Type:** `Unknown`

**Modifiers:** compute

---

### `jobTypes`

**Type:** `Unknown`

**Modifiers:** compute

---

### `workers`

**Type:** `[PayrollWorker]?`

**Modifiers:** compute

---

## Functions

### `nextN`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `itemRoles`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

## Views

### `form`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

