# IncomeStatement

**Type:** report  
**App:** flow2b.acc

## Fields

### `legalEntity`

**Type:** `OurLegalEntity?`

---

### `from`

**Type:** `Date`

---

### `to`

**Type:** `Date`

---

## Functions

### `baseCurrency`

---

### `baseQuery`

---

### `netIncome`

**Returns:** `Future[Money[baseCurrency]?]`

**Modifiers:** back

---

### `taxIncome`

**Returns:** `Future[Money[baseCurrency]?]`

**Modifiers:** back

---

### `accountSubTypes`

**Returns:** `Future[[LedgerAccountSubType : Income]?]`

**Modifiers:** back

---

## Views

### `list`

**Modifiers:** impl

---

