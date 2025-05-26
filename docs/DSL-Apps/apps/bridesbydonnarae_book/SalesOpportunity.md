# SalesOpportunity

**Type:** entity  
**App:** bridesbydonnarae.book

**Extends:** [`HasN`](../core/HasN.md)

**Implements:** `Entity with IActiveItem`

## Fields

### `customer`

**Type:** `Customer by opportunities`

**Modifiers:** ref

---

### `person`

**Type:** `Unknown`

**Modifiers:** compute

---

### `measurments`

**Type:** `PerMeasurments?`

---

### `appointments`

**Type:** `[BridalAppointment]? read by opportunity`

---

### `details`

**Type:** `BridalDetails?`

---

### `salesOrders`

**Type:** `[SalesOrder]? read by opportunity`

---

### `contacts`

**Type:** `Unknown`

**Modifiers:** compute

---

### `dresses`

**Type:** `[OpportunityDress]? inline by opportunity`

---

### `bridalAppointment`

**Type:** `Unknown`

**Modifiers:** compute

---

### `fittingAppointment`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `canRead`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `entitySubject`

**Modifiers:** override

---

### `personTo`

---

### `calcState`

**Returns:** `OpportunityState`

---

### `nextN`

**Modifiers:** impl

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

