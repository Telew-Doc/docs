# IBaseProduct

**Type:** extend trait  
**App:** flow2b.product

**Modifiers:** extend

## Fields

### `currentPrice`

**Type:** `UMoney?`

**Modifiers:** compute

---

### `regularPrice`

**Type:** `UMoney?`

**Modifiers:** compute

---

### `ourPrices`

**Type:** `[IPrice]?`

**Modifiers:** compute

---

### `purchasePrices`

**Type:** `[IPrice]?`

**Modifiers:** compute

---

### `prices`

**Type:** `Unknown`

**Modifiers:** compute

---

### `staticPrices`

**Type:** `[IStaticPrice]? inline by product`

---

### `dynamicPrices`

**Type:** `[IPrice]?`

**Modifiers:** compute

---

### `possibleOurModels`

**Type:** `Unknown`

**Modifiers:** compute

---

### `possibleTheirModels`

**Type:** `Unknown`

**Modifiers:** compute

---

## Functions

### `defPriceSales`

---

### `updateSalesPrice`

**Returns:** `Void`

---

### `updateRentPrice`

**Returns:** `Void`

---

### `prevPriceModel`

**Returns:** `IPriceModel?`

**Modifiers:** back

---

