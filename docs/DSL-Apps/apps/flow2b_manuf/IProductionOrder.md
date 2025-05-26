# IProductionOrder

**Type:** trait  
**App:** flow2b.manuf

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `Journal with IProdMoveIn with IProdMoveOut`

## Fields

### `outputStockType`

**Type:** `StockInvType`

---

### `refNum`

**Type:** `String?`

**Modifiers:** ref

---

### `dispatchDate`

**Type:** `Date`

**Modifiers:** ref

---

### `deliveryDate`

**Type:** `Date`

**Modifiers:** ref

---

### `status`

**Type:** `ProductionOrderStatus`

**Modifiers:** ref

---

### `factory`

**Type:** `IStore`

---

### `sSupplier`

**Type:** `OurLegalEntity?`

---

### `supplier`

**Type:** `OurLegalEntity`

**Modifiers:** compute

---

### `sReceiver`

**Type:** `OurLegalEntity?`

---

### `receiver`

**Type:** `OurLegalEntity`

**Modifiers:** compute

---

### `sOutputStore`

**Type:** `IStore?`

---

### `outputStore`

**Type:** `IStore`

**Modifiers:** compute

---

### `sMaterialStore`

**Type:** `IStore?`

---

### `materialStore`

**Type:** `IStore`

**Modifiers:** compute

---

## Functions

### `materials`

**Returns:** `[IProMaterial]?`

---

### `outputs`

**Returns:** `[IProOutput]?`

---

### `moveItems`

**Modifiers:** override

---

### `moveOutState`

**Modifiers:** impl

---

### `moveOutLE`

**Modifiers:** impl

---

### `moveOutStore`

**Modifiers:** impl

---

### `moveOutItems`

**Modifiers:** impl

---

### `moveInDate`

**Modifiers:** impl

---

### `moveInState`

**Modifiers:** impl

---

### `moveInLE`

**Modifiers:** impl

---

### `moveInStore`

**Modifiers:** impl

---

### `moveInItems`

**Modifiers:** impl

---

### `itemRoles`

**Modifiers:** override

---

### `entityNumbers`

**Modifiers:** impl

---

### `number`

**Returns:** `String`

---

### `itemOrder`

**Modifiers:** override

---

### `journalDate`

**Modifiers:** impl

---

### `qty`

**Returns:** `UQty`

---

### `mainProduct`

**Returns:** `OutputProduct`

---

