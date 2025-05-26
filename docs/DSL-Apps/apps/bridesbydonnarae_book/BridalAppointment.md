# BridalAppointment

**Type:** entity  
**App:** bridesbydonnarae.book

**Extends:** [`Event`](../flow2b_trip/Event.md)

**Implements:** `EventParticipant`

## Fields

### `opportunity`

**Type:** `SalesOpportunity by appointments`

**Modifiers:** ref

---

### `type`

**Type:** `ApptType`

**Modifiers:** ref

---

### `state`

**Type:** `ApptState`

**Modifiers:** ref

---

### `cancelDate`

**Type:** `Date?`

**Modifiers:** system

---

### `person`

**Type:** `Person`

**Modifiers:** compute

---

### `salesperson`

**Type:** `Person`

**Modifiers:** ref

---

### `periods`

**Type:** `Future[[RentAvPeriodItem]?]`

**Modifiers:** compute

---

## Functions

### `personTo`

**Returns:** `[Person]?`

---

### `event`

**Modifiers:** impl

---

### `participant`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `active`

**Modifiers:** override

---

### `issueTypes`

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

### `traitItem`

**Modifiers:** impl

---

