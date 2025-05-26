# Activity

**Type:** entity  
**App:** core

**Modifiers:** inline

## Fields

### `dateTime`

**Type:** `Date`

---

### `user`

**Type:** `IUser`

---

### `isPublic`

**Type:** `Bool`

**Modifiers:** compute

---

### `isSupport`

**Type:** `Bool`

**Modifiers:** compute

---

### `thread`

**Type:** `Int?`

---

### `to`

**Type:** `[IContact]?`

---

### `from`

**Type:** `Contact?`

---

### `author`

**Type:** `Contact`

**Modifiers:** compute

---

### `data`

**Type:** `Any`

**Modifiers:** system

---

### `messageId`

**Type:** `String?`

**Modifiers:** system

---

### `channel`

**Type:** `CommChannel?`

---

### `comment`

**Type:** `Text?`

---

### `files`

**Type:** `[File]?`

**Modifiers:** compute

---

### `deliveries`

**Type:** `[ActivityDelivery]?`

---

### `allDeliveries`

**Type:** `[ActivityDelivery]?`

**Modifiers:** compute

---

### `patches`

**Type:** `[Entity: Patch]?`

**Modifiers:** system

---

### `template`

**Type:** `NotifyTemplate[RefEntity]?`

---

### `templateEntity`

**Type:** `RefEntity?`

---

### `_subject`

**Type:** `String?`

---

### `subject`

**Type:** `String`

**Modifiers:** compute

---

### `recipients`

**Type:** `[Contact]?`

**Modifiers:** compute

---

## Functions

### `getTemplateEntity`

---

### `current`

**Returns:** `Activity?`

**Modifiers:** native, object

---

### `comment`

**Returns:** `Void`

---

### `mainEntity`

**Returns:** `Entity`

---

### `setMainEntity`

**Returns:** `Void`

---

### `makePublic`

**Returns:** `Void`

---

### `makeSupport`

**Returns:** `Void`

---

### `shortComment`

**Returns:** `Text?`

**Modifiers:** back

---

### `recipientsString`

**Returns:** `String?`

---

### `hasRecipient`

**Returns:** `Bool`

---

### `forward`

**Returns:** `Void`

---

### `resend`

**Returns:** `Void`

**Modifiers:** back

---

### `ignore`

**Returns:** `Void`

**Modifiers:** back

---

### `releaseHold`

**Returns:** `Void`

**Modifiers:** back

---

### `cancelHold`

**Returns:** `Void`

**Modifiers:** back

---

### `send`

**Returns:** `Void`

**Modifiers:** back

---

### `reply`

**Returns:** `Void`

---

### `to`

**Returns:** `Void`

---

### `to`

**Returns:** `Void`

---

### `hasSubject`

---

## Views

### `newForm`

---

