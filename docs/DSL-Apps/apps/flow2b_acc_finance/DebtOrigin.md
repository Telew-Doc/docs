# DebtOrigin

**Type:** trait  
**App:** flow2b.acc.finance

**Extends:** [`Journal`](../flow2b_acc_base/Journal.md)

## Fields

### `calcDebtAllowance`

**Type:** `Money?`

**Modifiers:** compute

---

### `debtUnpaidAmount`

**Type:** `Money[debtCurrency]?`

**Modifiers:** compute

---

### `unreconAmount`

**Type:** `Money[debtCurrency]?`

**Modifiers:** compute

---

### `calcReconAmount`

**Type:** `Money?`

**Modifiers:** compute

---

### `manLinks`

**Type:** `[DebtOrigin]? by manLinks`

---

### `debtOriginAmounts`

**Type:** `[OriginAmount]?`

**Modifiers:** compute

---

## Functions

### `debtCurrency`

**Returns:** `Currency`

---

### `debtAmount`

**Returns:** `Money[debtCurrency]?`

---

### `debtCounterparty`

**Returns:** `LegalEntity?`

---

### `isLowPriorityDebt`

---

### `isPurchase`

**Returns:** `Bool`

---

### `isInstant`

**Returns:** `Bool //No debt account has been used to pay taxed amount`

---

### `canRead`

**Modifiers:** impl

---

### `noCpTitle`

---

### `unrecon`

**Returns:** `Bool`

---

### `recon`

**Returns:** `Bool`

---

### `mainOrigin`

**Returns:** `DebtOrigin`

---

### `allOrigins`

**Returns:** `[DebtOrigin]?`

---

### `considerManLinks`

**Modifiers:** object

---

### `allManLinks`

**Returns:** `[DebtOrigin]?`

---

### `debtLedgers`

**Returns:** `[LMoneyDebt]?`

**Modifiers:** back

---

### `debtCashFlows`

**Returns:** `[CashFlowAmount]?`

**Modifiers:** back

---

### `debtOrigins`

**Returns:** `[DebtOrigin]?`

**Modifiers:** back

---

### `paymentCashFlows`

**Returns:** `[CashFlowAmount]?`

**Modifiers:** back

---

