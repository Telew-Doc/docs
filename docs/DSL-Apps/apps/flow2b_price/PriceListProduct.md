# PriceListProduct

**Type:** entity  
**App:** flow2b.price

**Extends:** [`IStaticPriceSales`](../flow2b_product/IStaticPriceSales.md)

## Fields

### `priceList`

**Type:** `PriceList by products`

---

### `regular`

**Type:** `UMoney[currency]?`

---

### `gstK`

**Type:** `Unknown`

**Modifiers:** compute

---

### `current`

**Type:** `UMoney[currency]?`

---

### `cost`

**Type:** `Future[UMoney[currency]?]`

**Modifiers:** compute

---

### `regularMargin`

**Type:** `Percent[2]?`

**Modifiers:** compute

---

### `currentMargin`

**Type:** `Percent[2]?`

**Modifiers:** compute

---

## Functions

### `model`

**Modifiers:** impl

---

### `autoCategories`

**Modifiers:** impl

---

### `autoTags`

**Modifiers:** impl

---

### `margin`

**Returns:** `Percent[2]?`

---

### `priceWithMargin`

**Returns:** `UMoney[currency]?`

---

### `salesPrice`

**Returns:** `Future[SalesPrice]`

**Modifiers:** impl

---

### `updateSalesPrice`

**Returns:** `Bool`

**Modifiers:** impl

---

## Views

### `rowView`

---

### `row2View`

---

### `form`

**Modifiers:** override

---

