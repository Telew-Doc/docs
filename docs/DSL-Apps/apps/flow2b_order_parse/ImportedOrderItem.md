# ImportedOrderItem

**Type:** entity  
**App:** flow2b.order.parse

**Modifiers:** inline

## Fields

### `order`

**Type:** `ImportedOrder by items`

---

### `code`

**Type:** `String?`

---

### `desc`

**Type:** `PlainText?`

---

### `qty`

**Type:** `Qty?`

---

### `amount`

**Type:** `Money[order.currency]?`

---

### `gstRate`

**Type:** `UPercent[2]??`

---

### `gstAmount`

**Type:** `Money[order.currency]?`

**Modifiers:** compute

---

### `amountNoGst`

**Type:** `Unknown`

**Modifiers:** compute

---

### `amountWithGst`

**Type:** `Unknown`

**Modifiers:** compute

---

### `gstIssue`

**Type:** `Bool`

---

### `gstRateEditor`

**Type:** `UPercent[2]?`

**Modifiers:** compute

---

