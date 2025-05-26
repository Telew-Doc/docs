# MarketingProduct

**Type:** entity  
**App:** flow2b.net.marketing

**Extends:** [`WebPage`](../flow2b_net_marketing/WebPage.md)

## Fields

### `status`

**Type:** `PublicationStatus`

---

### `group`

**Type:** `MarketingProductGroup by products`

---

### `readiness`

**Type:** `Readiness`

---

### `devProducts`

**Type:** `[DevProduct]?`

---

### `advantages`

**Type:** `[ProductAdvantage]? read by product`

---

### `niches`

**Type:** `[ProductNiche]? inline by product`

---

## Functions

### `anchor`

---

### `htmlName`

---

### `html`

**Returns:** `Html`

---

### `groupHtml`

**Returns:** `Html`

---

### `indexIndustry`

**Returns:** `ProductNiche`

---

## Views

### `form`

**Modifiers:** impl

---

