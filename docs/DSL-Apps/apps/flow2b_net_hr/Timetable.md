# Timetable

**Type:** entity  
**App:** flow2b.net.hr

**Extends:** [`HasN`](../core/HasN.md)

## Fields

### `complete`

**Type:** `Bool`

---

### `date`

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

### `worker`

**Type:** `Worker`

**Modifiers:** ref

---

### `rows`

**Type:** `[TimetableRow] inline by timetable`

---

### `totalTime`

**Type:** `Time`

**Modifiers:** compute

---

## Functions

### `nextN`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `jobTypes`

---

## Views

### `form`

**Modifiers:** impl

---

