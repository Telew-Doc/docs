# BookApi

**Type:** entity  
**App:** bridesbydonnarae.book

**Extends:** [`SystemService`](../core/SystemService.md)

**Implements:** `IEndpoint`

## Fields

### `model`

**Type:** `BookPriceModel`

---

### `bridalProduct`

**Type:** `JobType`

**Modifiers:** ref

---

### `fittingProduct`

**Type:** `JobType`

**Modifiers:** ref

---

### `legalEntity`

**Type:** `OurLegalEntity`

---

### `store`

**Type:** `IStore`

---

### `fittingConfirm`

**Type:** `PlainText`

---

### `bridalConfirm`

**Type:** `PlainText`

---

## Functions

### `one`

**Returns:** `BookApi`

**Modifiers:** object

---

### `title`

**Modifiers:** impl

---

### `service`

**Modifiers:** impl

---

### `canRead`

**Modifiers:** impl

---

### `canWrite`

**Modifiers:** impl

---

### `postNewAppointment`

**Returns:** `NewApptResponse`

**Modifiers:** back

---

### `getPeriods`

**Returns:** `PeriodsResponse`

**Modifiers:** back

---

### `postSelectPeriod`

**Returns:** `Future[ConfirmResponse]`

**Modifiers:** back

---

### `postDetails`

**Returns:** `ConfirmResponse`

**Modifiers:** back

---

### `opportunity`

**Returns:** `SalesOpportunity`

**Modifiers:** back

---

### `product`

**Returns:** `JobType`

**Modifiers:** back

---

### `rentAvPeriods`

**Modifiers:** back

---

### `rentCalcItem`

**Modifiers:** back

---

## Views

### `form`

**Modifiers:** impl

---

