# OrderProductItem

**Type:** trait  
**App:** flow2b.inv.order

**Modifiers:** inline

**Extends:** [`OrderItem`](../flow2b_inv_order/OrderItem.md)

**Implements:** `IOrderProdItem with IAmountQtyItem with IncomeRecodable`

## Fields

### `itemDesc`

**Type:** `Text?`

**Modifiers:** compute

---

### `nonTaxable`

**Type:** `UPercent?`

---

### `taxable`

**Type:** `UPercent?`

**Modifiers:** compute

---

### `accessories`

**Type:** `[ISubProduct]?`

**Modifiers:** compute

---

## Functions

### `orderDlvItem`

**Returns:** `IOrderDlvItem?`

**Modifiers:** impl

---

### `product`

**Modifiers:** impl

---

### `baseQty`

---

### `priceOrderItem`

**Modifiers:** impl

---

### `defaultGstRate`

**Modifiers:** impl

---

### `qty`

**Modifiers:** impl

---

### `invoiceQty`

**Returns:** `UQty?`

**Modifiers:** impl

---

### `hasProgress`

**Modifiers:** impl

---

### `unit`

---

### `needsRevision`

**Returns:** `Bool`

**Modifiers:** override

---

### `sameAsPrev`

**Modifiers:** override

---

### `invoiceDesc`

**Modifiers:** override

---

### `name`

**Returns:** `String`

**Modifiers:** impl

---

### `fullDesc`

**Modifiers:** override

---

### `recode`

**Returns:** `Void`

**Modifiers:** impl

---

### `income`

**Modifiers:** impl

---

### `doRepeat`

**Modifiers:** override

---

