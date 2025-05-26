# OrderDlv

**Type:** trait  
**App:** flow2b.inv.order

**Extends:** [`IOrderDlv`](../flow2b_invoice/IOrderDlv.md)

**Implements:** `Journal with HasNumber`

## Fields

### `_state`

**Type:** `DlvState`

**Modifiers:** ref

---

### `start`

**Type:** `Date`

**Modifiers:** ref

---

### `end`

**Type:** `Date?`

**Modifiers:** ref

---

### `allItems`

**Type:** `[IOrderDlvItem]? inline by delivery`

---

### `repeat`

**Type:** `DlvRepeat? inline by dlv`

---

### `next`

**Type:** `OrderDlv? by prev`

**Modifiers:** const

---

### `prev`

**Type:** `OrderDlv? by next`

**Modifiers:** const

---

### `items`

**Type:** `[IOrderDlvItem]?`

**Modifiers:** compute

---

### `canceled`

**Type:** `Bool`

**Modifiers:** compute

---

### `planned`

**Type:** `Bool`

**Modifiers:** compute

---

### `schedule`

**Type:** `Unknown`

**Modifiers:** compute

---

### `retSchedule`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `store`

**Returns:** `IStore?`

---

### `retStore`

**Returns:** `IStore?`

---

### `orders`

**Returns:** `[Order]`

**Modifiers:** impl

---

### `priceLevel`

**Returns:** `IPriceLevel`

---

### `needLedgers`

**Returns:** `Bool`

---

### `dlvLocOwners`

**Returns:** `[LegalEntity]?`

---

### `counterparty`

**Returns:** `LegalEntity?`

---

### `ledgers`

**Returns:** `Future[[Ledger]?]`

**Modifiers:** back

---

### `doRepeat`

**Returns:** `Future[OrderDlv?]`

**Modifiers:** back

---

### `stockType`

**Returns:** `StockInvType`

---

### `journalDate`

**Modifiers:** impl

---

### `dlvItems`

**Modifiers:** impl

---

### `dlvPrePath`

**Modifiers:** impl

---

### `dlvPostPath`

**Modifiers:** impl

---

### `dlvOrderStates`

**Modifiers:** impl

---

### `dlvInProgessDate`

**Modifiers:** impl

---

### `dlvCompleteDate`

**Modifiers:** impl

---

### `invTitle`

**Returns:** `String`

---

### `hasProgress`

---

### `isInstant`

**Modifiers:** back

---

### `startShDate`

---

### `endShDate`

---

### `stateUpdated`

**Returns:** `Future[Void]`

---

### `updateDlvPeriod`

**Returns:** `Future[Period]`

---

### `adjustDate`

**Returns:** `Future[Date]`

---

### `calcDlvPeriod`

**Returns:** `Future[Period]`

---

### `updateDurs`

**Returns:** `Future[Void]`

---

### `salesLedgers`

**Returns:** `Future[[Ledger]?]`

**Modifiers:** back

---

### `purchaseLedgers`

**Returns:** `Future[[Ledger]?]`

**Modifiers:** back

---

### `order`

**Returns:** `Order`

---

### `dlvStates`

**Returns:** `[DlvState]`

---

## Views

### `invRow`

**Modifiers:** impl

---

