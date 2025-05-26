# BankData

**Type:** class  
**App:** flow2b.payment

## Fields

### `bankId`

**Type:** `String?`

---

### `type`

**Type:** `String?`

---

### `memo`

**Type:** `String?`

---

### `thierName`

**Type:** `String?`

---

### `thierAccount`

**Type:** `String?`

---

### `cardNumber`

**Type:** `String?`

---

### `bankComment`

**Type:** `String?`

---

### `balance`

**Type:** `Money??`

---

### `uploadState`

**Type:** `BankUploadState`

**Modifiers:** system

---

### `date`

**Type:** `Date?`

**Modifiers:** system

---

### `itemType`

**Type:** `BankStmItemType?`

---

### `fee`

**Type:** `Money? // If negative then fees return. Fee should be included in the amount`

---

### `withholdingTax`

**Type:** `UMoney?`

---

### `currency`

**Type:** `Currency?`

---

### `amount`

**Type:** `Money?`

---

### `amountInCurrency`

**Type:** `Money?`

---

### `tax`

**Type:** `Tax?`

---

## Functions

### `uploaded`

**Returns:** `Bool`

---

### `fullMemo`

**Returns:** `String?`

---

### `initMethod`

**Returns:** `PMBankAccount`

---

### `forcePaymentMethod`

**Returns:** `PMBankAccount?`

**Modifiers:** back

---

### `addTo`

**Returns:** `Void`

**Modifiers:** back

---

## Views

### `form`

**Modifiers:** impl

---

