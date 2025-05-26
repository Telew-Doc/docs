# Appointment

**Type:** entity  
**App:** flow2b.organizer

**Extends:** [`Event`](../flow2b_trip/Event.md)

## Fields

### `roles`

**Type:** `[Role]?`

**Modifiers:** ref

---

### `participants`

**Type:** `[AppointmentParticipant] inline by appointment`

---

### `description`

**Type:** `Text?`

---

## Functions

### `numPrefix`

**Modifiers:** impl

---

### `issueTypes`

**Modifiers:** override

---

### `calcState`

**Returns:** `AppointmentState`

---

### `itemRoles`

**Modifiers:** impl

---

## Views

### `ref`

**Modifiers:** impl

---

### `traitItem`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

