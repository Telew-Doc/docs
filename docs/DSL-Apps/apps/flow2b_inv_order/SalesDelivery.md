# SalesDelivery

**Type:** entity  
**App:** flow2b.inv.order

**Extends:** [`ISalesDelivery`](../flow2b_inv_order/ISalesDelivery.md)

**Implements:** `IProdMoveOut with IProdMoveIn with DeferredJob`

## Fields

### `primary`

**Type:** `Bool`

---

### `_retStore`

**Type:** `IStore?`

---

### `shipToText`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `needLedgers`

**Modifiers:** impl

---

### `isProdMoveIn`

**Modifiers:** impl

---

### `priceLevel`

**Modifiers:** impl

---

### `dlvLocOwners`

**Modifiers:** impl

---

### `counterparty`

**Returns:** `LegalEntity?`

**Modifiers:** impl

---

### `moveItems`

**Modifiers:** override

---

### `moveOutSort`

**Modifiers:** override, front

---

### `moveOutState`

**Modifiers:** impl

---

### `moveOutLE`

**Modifiers:** impl

---

### `moveOutStore`

**Modifiers:** impl

---

### `moveOutItems`

**Modifiers:** impl

---

### `moveInDate`

**Modifiers:** impl

---

### `moveInState`

**Modifiers:** impl

---

### `moveInLE`

**Modifiers:** impl

---

### `moveInStore`

**Modifiers:** impl

---

### `moveInItems`

**Modifiers:** impl

---

### `itemOrder`

**Modifiers:** override

---

### `isReturnOverdue`

**Returns:** `Bool`

---

### `jobDate`

**Modifiers:** impl

---

### `do`

**Modifiers:** impl

---

### `service`

**Modifiers:** impl

---

### `entityNumbers`

**Modifiers:** override

---

### `orders`

**Returns:** `[Order]`

**Modifiers:** impl

---

### `legalEntity`

**Modifiers:** impl

---

### `title`

**Modifiers:** impl

---

### `canDispatch`

**Modifiers:** override

---

## Views

### `invRow`

**Modifiers:** override

---

### `deliveryHeader`

**Modifiers:** impl

---

### `form`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

### `dash`

**Modifiers:** impl

---

### `dashOut`

**Modifiers:** impl

---

### `dashIn`

**Modifiers:** impl

---

### `stateView`

---

