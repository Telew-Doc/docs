# IOrderItem

**Type:** trait  
**App:** flow2b.invoice

**Extends:** [`InlineEntity`](../core/InlineEntity.md)

## Fields

### `rollbacked`

**Type:** `Bool`

**Modifiers:** system

---

### `prev`

**Type:** `IOrderItem? by next`

**Modifiers:** system

---

### `next`

**Type:** `IOrderItem? by prev`

**Modifiers:** system

---

### `invoices`

**Type:** `[Invoice]? by items`

**Modifiers:** system

---

### `active`

**Type:** `Bool`

---

### `wasCanceled`

**Type:** `Bool`

---

### `itemRevisions`

**Type:** `[this]?`

**Modifiers:** compute

---

## Functions

### `order`

**Returns:** `IOrder`

---

### `currency`

**Returns:** `Currency`

---

### `gstAmount`

**Returns:** `Money[currency]?`

---

### `distributeGst`

---

### `invoiceQty`

**Returns:** `Qty?`

---

### `invoiceAmount`

**Returns:** `Money[currency]?`

---

### `invoiceAmountNoGst`

**Returns:** `Money[currency]?`

---

### `invoiceAmountWithGst`

**Returns:** `Money[currency]?`

---

### `ledgerAccount`

**Returns:** `LedgerAccount`

---

### `gstRate`

**Returns:** `UPercent[2]??`

---

### `itemDlv`

**Returns:** `IOrderDlv?`

---

### `canceled`

**Returns:** `Bool`

---

### `rowView`

**Returns:** `Layout[IOrderItem]`

---

### `labelView`

**Returns:** `Layout[IOrderItem]`

---

### `labelNoteView`

**Returns:** `Layout[IOrderItem]`

---

### `cashFlow`

**Returns:** `CashFlow`

---

### `hasProgress`

---

### `invoiceOrder`

**Returns:** `Dec[2]?`

---

### `invoicePosition`

**Returns:** `InvoiceItemPosition`

---

### `dropShipItem`

**Returns:** `IOrderItem?`

---

### `canBeDeleted`

---

### `rollbackItem`

**Returns:** `Void`

**Modifiers:** back

---

### `consider`

---

### `invoiceNotIssued`

---

### `rowView`

**Returns:** `Layout[IOrderItem]`

---

### `labelView`

**Returns:** `Layout[IOrderItem]`

---

### `setActive`

**Returns:** `Void`

---

### `prev`

**Returns:** `this?`

---

### `needsRevision`

**Returns:** `Bool`

---

### `sameAsPrev`

**Returns:** `Bool`

---

