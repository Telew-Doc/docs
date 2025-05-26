# ISubProduct

**Type:** extend trait  
**App:** flow2b.trademe

**Modifiers:** extend

## Fields

### `trademeStatus`

**Type:** `TrademeProductStatus?`

---

### `trademeSubtitle`

**Type:** `String?`

---

### `_trademePromotion`

**Type:** `TrademePromotion?`

---

### `trademePromotion`

**Type:** `TrademePromotion?`

**Modifiers:** compute

---

### `_trademeTemplates`

**Type:** `[TrademeTemplate]?`

---

### `trademeTemplates`

**Type:** `[TrademeTemplate]?`

**Modifiers:** compute

---

### `_trademeTitle`

**Type:** `String?`

---

### `trademeTitle`

**Type:** `String`

**Modifiers:** compute

---

### `_trademeDescription`

**Type:** `PlainText?`

---

### `trademeDescription`

**Type:** `PlainText?`

**Modifiers:** compute

---

### `_trademeCategories`

**Type:** `[TrademeCategory]?`

---

### `trademeCategories`

**Type:** `[TrademeCategory]?`

**Modifiers:** compute

---

### `_trademePhotos`

**Type:** `[Image]?`

---

### `trademePhotos`

**Type:** `[Image]?`

**Modifiers:** compute

---

### `trademeStartPrice`

**Type:** `Money[NZD]?`

---

### `trademeReservePrice`

**Type:** `Money[NZD]?`

---

### `tmUrls`

**Type:** `[Url]?`

**Modifiers:** compute

---

### `trademeBuyNowPrice`

**Type:** `Money[NZD]?`

---

## Functions

### `_collectTrademePhotos`

**Returns:** `[Image]?`

**Modifiers:** override

---

### `hasAuction`

---

### `updateTrademe`

**Returns:** `Void`

**Modifiers:** back

---

## Events

### `onSave` (back)

---

