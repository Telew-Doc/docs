# DevQuote

**Type:** entity  
**App:** flow2b.net.sales

**Extends:** [`HasN`](../core/HasN.md)

## Fields

### `date`

**Type:** `Date`

**Modifiers:** ref

---

### `customer`

**Type:** `Customer by quotes`

**Modifiers:** ref

---

### `currency`

**Type:** `Unknown`

**Modifiers:** compute

---

### `cancelled`

**Type:** `Bool`

---

### `items`

**Type:** `[DevQuoteItem] inline by quote`

---

### `ready`

**Type:** `Unknown`

**Modifiers:** compute

---

### `order`

**Type:** `SalesOrder? by quotes`

---

### `estimation`

**Type:** `Estimation?`

**Modifiers:** compute

---

## Functions

### `calcState`

**Returns:** `QuoteState`

---

### `numPrefix`

**Modifiers:** impl

---

### `nextN`

**Modifiers:** impl

---

### `makeOrder`

**Returns:** `SalesOrder`

**Modifiers:** back

---

## Views

### `form`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

