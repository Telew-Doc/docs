# AnyEntity

**Type:** trait  
**App:** core

**Extends:** [`AnyRef`](../core/AnyRef.md)

## Functions

### `workspaceId`

**Returns:** `UInt`

**Modifiers:** native

---

### `canRead`

---

### `canWrite`

---

### `all`

**Returns:** `QueryN[this]`

**Modifiers:** native, object

---

### `search`

**Returns:** `QueryN[this]`

**Modifiers:** native, object

---

### `allWithDeleted`

**Returns:** `QueryN[this]`

**Modifiers:** native, object

---

### `load`

**Returns:** `Query1[this]`

**Modifiers:** native, object

---

### `uuid`

**Returns:** `Query1[this]`

**Modifiers:** native, object

---

### `save`

**Returns:** `this`

**Modifiers:** native

---

### `delete`

**Returns:** `this`

**Modifiers:** native

---

### `touch`

**Returns:** `this`

**Modifiers:** native

---

### `updateRegisters`

**Returns:** `this`

**Modifiers:** native

---

### `forceTouch`

**Returns:** `this`

**Modifiers:** native

---

### `created`

**Returns:** `Bool`

**Modifiers:** native

---

### `updated`

**Returns:** `Bool`

**Modifiers:** native

---

### `dataUpdated`

**Returns:** `Bool`

**Modifiers:** native

---

### `registerUpdated`

**Returns:** `Bool`

**Modifiers:** native

---

### `touched`

**Returns:** `Bool`

**Modifiers:** native

---

### `deleted`

**Returns:** `Bool`

**Modifiers:** native

---

### `updateWith`

**Returns:** `Void`

**Modifiers:** native

---

### `canReplaceWith`

---

### `entityText`

**Returns:** `PlainText?`

**Modifiers:** native

---

### `converters`

**Returns:** `[Converter]?`

---

### `multiupdate`

**Returns:** `[AnyEntity]?`

---

### `preComputeItems`

**Returns:** `[AnyEntity]?`

**Modifiers:** back

---

### `apiUrl`

**Returns:** `Url`

**Modifiers:** back

---

### `apiUrl`

**Returns:** `Url`

**Modifiers:** back

---

### `saveBy`

**Returns:** `this`

**Modifiers:** back

---

## Views

### `quick`

---

## Events

### `onLoad` (front)

**Returns:** `F`

---

### `onOpen` (front)

**Returns:** `F`

---

### `preDelete` (back)

**Returns:** `V`

---

### `onActivity` (back)

**Returns:** `V`

---

### `onSave` (back)

**Returns:** `F`

---

### `onDelete` (back)

**Returns:** `F`

---

### `onSaveOrDelete` (back)

**Returns:** `F`

---

