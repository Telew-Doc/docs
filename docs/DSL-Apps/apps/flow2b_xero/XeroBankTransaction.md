# XeroBankTransaction

**Type:** class  
**App:** flow2b.xero

## Fields

### `bankTransactionID`

**Type:** `String?`

---

### `type`

**Type:** `XeroBankTransactionType?`

---

### `contact`

**Type:** `XeroContact?`

---

### `lineItems`

**Type:** `[XeroBankTransactionLineItem]?`

---

### `bankAccount`

**Type:** `XeroBankAccount?`

---

### `isReconciled`

**Type:** `Bool?`

---

### `date`

**Type:** `Date?`

---

### `reference`

**Type:** `String?`

**Modifiers:** ref

---

### `currencyCode`

**Type:** `Currency?`

---

### `currencyRate`

**Type:** `Dec?`

---

### `url`

**Type:** `Url?`

---

### `status`

**Type:** `XeroBankTransactionStatus?`

---

### `lineAmountTypes`

**Type:** `XeroLineAmountTypes`

---

### `subTotal`

**Type:** `Money?`

---

### `totalTax`

**Type:** `Money?`

---

### `total`

**Type:** `Money?`

---

### `prepaymentID`

**Type:** `String?`

---

### `overpaymentID`

**Type:** `String?`

---

### `updatedDateUTC`

**Type:** `Date?`

---

### `hasAttachments`

**Type:** `Bool?`

---

### `isNegative`

**Type:** `Bool`

**Modifiers:** compute

---

### `finalType`

**Type:** `XeroBankTransactionType`

**Modifiers:** compute

---

## Functions

### `totalMoney`

**Returns:** `UMoney`

---

