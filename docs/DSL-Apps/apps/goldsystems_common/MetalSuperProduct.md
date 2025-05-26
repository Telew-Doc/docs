# MetalSuperProduct

**Type:** trait  
**App:** goldsystems.common

**Extends:** [`ISuperProduct`](../flow2b_inv_move/ISuperProduct.md)

**Implements:** `IMetalSuperProduct with IWeightSize`

## Fields

### `totalWeightOz`

**Type:** `UQty[ProductUnit.Ounce, 5]`

**Modifiers:** compute

---

### `puritySelection`

**Type:** `Purity?`

**Modifiers:** compute

---

### `purity`

**Type:** `UDec[5]`

**Modifiers:** ref

---

### `pureWeight`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `isTangible`

**Returns:** `Bool`

**Modifiers:** impl

---

### `metalProducts`

**Returns:** `[MetalSuperProduct: UQty]`

**Modifiers:** impl

---

### `isMetalProduct`

**Modifiers:** impl

---

### `size`

**Returns:** `UQty[sizeUnit, 5]`

---

### `sizeUnit`

**Returns:** `ProductUnit`

---

### `weightUnit`

**Modifiers:** impl

---

### `weight`

**Modifiers:** impl

---

### `gstRate`

**Returns:** `UPercent[2]??`

**Modifiers:** override

---

### `puteWeightUpdated`

**Returns:** `Void`

---

