# SalesOrder

**Type:** entity  
**App:** flow2b.inv.order

**Extends:** [`Order`](../tubularequipment_wf/Order.md)

**Implements:** `ISalesOrder`

## Fields

### `sPayer`

**Type:** `Customer?`

---

### `_receiver`

**Type:** `LegalEntity?`

**Modifiers:** compute

---

### `receiver`

**Type:** `LegalEntity?`

**Modifiers:** compute

---

### `shipTo`

**Type:** `ILocation?`

**Modifiers:** compute

---

### `shipToText`

**Type:** `Unknown`

**Modifiers:** compute

---

### `salesChannel`

**Type:** `ISalesChannel?`

---

### `sd`

**Type:** `Unknown`

**Modifiers:** compute

---

### `prevOrder`

**Type:** `Unknown`

**Modifiers:** compute

---

### `nextOrder`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `orderCustomer`

**Modifiers:** impl

---

### `orderVendor`

**Modifiers:** impl

---

### `counterparty`

---

### `salesPersonAccess`

---

### `deliveryCounterparty`

**Modifiers:** impl

---

### `debtCounterparty`

**Returns:** `LegalEntity?`

**Modifiers:** impl

---

### `multiupdate`

**Modifiers:** impl

---

### `issueTypes`

**Modifiers:** override

---

### `itemRoles`

**Modifiers:** impl

---

### `addItem`

**Returns:** `Future[OrderItem]`

**Modifiers:** impl

---

### `isTheir`

---

### `numPrefix`

**Modifiers:** impl

---

### `entityNumbers`

**Modifiers:** override

---

### `title`

**Modifiers:** impl

---

### `legalEntity`

**Modifiers:** impl

---

### `activeItemType`

**Modifiers:** override

---

## Views

### `form`

**Modifiers:** impl

---

### `stateView`

---

### `posView`

---

### `ref`

**Modifiers:** impl

---

### `dash`

**Modifiers:** impl

---

