# IOrderRevision

**Type:** trait  
**App:** flow2b.invoice

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `DebtOrigin`

## Fields

### `gstAmount`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `invoiceSubtotalNoGst`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `invoiceTotalNoGst`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `invoicePayments`

**Type:** `[OrderDebtRow]?`

**Modifiers:** compute

---

### `invoiceOffsets`

**Type:** `[OrderDebtRow]?`

**Modifiers:** compute

---

### `invoicePaidAmount`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `invoiceOffsetAmount`

**Type:** `Money[currency]?`

**Modifiers:** compute

---

### `invoiceToPay`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `invoiceToRefund`

**Type:** `UMoney[currency]?`

**Modifiers:** compute

---

### `dueInvoices`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `paymentState`

**Returns:** `PaymentState`

---

### `currency`

**Returns:** `Currency`

---

### `date`

**Returns:** `Date`

---

### `items`

**Returns:** `[IOrderItem]?`

---

### `items0`

---

### `paid`

**Returns:** `Bool`

---

### `preComputeItems`

**Modifiers:** impl

---

### `debtCurrency`

**Modifiers:** impl

---

### `debtTotal`

---

### `canceled`

**Returns:** `Bool`

---

### `dueDate`

**Returns:** `Date?`

---

### `debtTable`

**Returns:** `[OrderDebtRow]?`

---

### `dueRate`

**Returns:** `Percent[2]?`

---

### `unpaidAmount`

**Returns:** `Money[currency]?`

---

### `totalDue`

**Returns:** `Money[currency]?`

---

### `order`

**Returns:** `IOrder`

---

### `number`

**Returns:** `String`

---

### `prev`

**Returns:** `Invoice?`

---

### `isNote`

---

### `allRevisions`

---

