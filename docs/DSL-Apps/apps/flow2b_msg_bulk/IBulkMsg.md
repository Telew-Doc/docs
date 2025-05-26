# IBulkMsg

**Type:** trait  
**App:** flow2b.msg.bulk

**Extends:** [`Entity`](../flow2b_msg/Entity.md)

**Implements:** `HasN`

## Fields

### `lists`

**Type:** `[SubscrList] by messages`

---

### `state`

**Type:** `BulkMsgState`

**Modifiers:** ref

---

### `_subject`

**Type:** `String?`

---

### `subject`

**Type:** `String`

**Modifiers:** compute

---

### `text`

**Type:** `Text?`

---

### `deliveries`

**Type:** `[BulkMsgDelivery]? inline by msg`

---

## Functions

### `nextN`

**Modifiers:** impl

---

### `numPrefix`

**Modifiers:** impl

---

### `itemRoles`

**Modifiers:** impl

---

### `issueTypes`

**Modifiers:** override

---

### `canAttachReply`

**Returns:** `Bool`

**Modifiers:** impl

---

### `subject`

**Returns:** `String`

---

### `text`

**Returns:** `Text?`

---

### `send`

**Returns:** `Void`

**Modifiers:** back

---

## Views

### `form`

**Modifiers:** impl

---

### `ref`

**Modifiers:** impl

---

### `traitItem`

**Modifiers:** impl

---

