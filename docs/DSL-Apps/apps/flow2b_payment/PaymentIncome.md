# PaymentIncome

**Type:** trait  
**App:** flow2b.payment

**Extends:** [`InlineEntity`](../core/InlineEntity.md)

**Implements:** `IReason with IncomeRecodable`

## Fields

### `nonTaxable`

**Type:** `UPercent?`

---

### `taxable`

**Type:** `UPercent?`

**Modifiers:** compute

---

### `gstAmount`

**Type:** `UMoney[payment.currency]?`

**Modifiers:** compute

---

### `taxableGstAmount`

**Type:** `UMoney[payment.currency]?`

**Modifiers:** compute

---

### `taxableIncomeAmount`

**Type:** `UMoney[payment.currency]?`

**Modifiers:** compute

---

### `incomeAmount`

**Type:** `UMoney[payment.currency]?`

**Modifiers:** compute

---

### `capitalAmount`

**Type:** `UMoney[payment.currency]?`

**Modifiers:** compute

---

### `gstRate`

**Type:** `UPercent[2]??`

---

### `gstValue`

**Type:** `UPercent[2]?`

**Modifiers:** compute

---

### `hasGst`

**Type:** `Bool`

**Modifiers:** compute

---

### `desc`

**Type:** `Text?`

---

## Functions

### `vendor`

**Returns:** `LegalEntity?`

---

### `recode`

**Returns:** `Void`

**Modifiers:** impl

---

### `currentAccount`

**Returns:** `CurrentAccount?`

---

### `calcGstRate`

**Returns:** `UPercent[2]??`

---

### `effectiveGstRate`

---

## Views

### `gstEditor`

---

