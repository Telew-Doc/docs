# Order

**Type:** trait  
**App:** flow2b.inv.order

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `Journal with HasDebtCounterparty with IOrder with HasN`

## Fields

### `rentPeriod`

**Type:** `Period?`

**Modifiers:** compute

---

### `referenceNumber`

**Type:** `Unknown`

**Modifiers:** ref, compute

---

### `dlvStart`

**Type:** `Date`

**Modifiers:** compute

---

### `totalWithGst`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `totalNoGst`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `gst`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `refItems`

**Type:** `Unknown`

**Modifiers:** ref, compute

---

## Functions

### `orderCustomer`

**Returns:** `ICustomer?`

**Modifiers:** impl

---

### `orderVendor`

**Returns:** `IVendor?`

**Modifiers:** impl

---

### `priceLevel`

**Returns:** `IPriceLevel`

---

### `nextN`

**Modifiers:** impl

---

### `processFixes`

**Modifiers:** override

---

### `cancelFixes`

**Modifiers:** override

---

### `entitySubject`

**Modifiers:** override

---

### `references`

**Modifiers:** impl

---

### `isQuote`

---

### `pricesIncludingGst`

**Returns:** `Bool`

---

### `itemOrder`

**Modifiers:** override

---

### `preEntered`

**Returns:** `Bool`

---

### `deliveries`

**Returns:** `[OrderDlv]`

**Modifiers:** impl

---

### `nakedN`

---

### `calcInstant`

**Modifiers:** impl

---

### `procBarcode`

**Returns:** `Future[Void]`

**Modifiers:** front

---

### `procNfc`

**Returns:** `Future[Void]`

**Modifiers:** front

---

### `addQty`

**Returns:** `Future[OrderItem]`

---

### `addItem`

**Returns:** `Future[OrderItem]`

---

### `orderCurrency`

---

### `orderTotal`

---

### `updateDispatchDate`

**Returns:** `Void`

**Modifiers:** impl

---

### `priceRequest`

---

