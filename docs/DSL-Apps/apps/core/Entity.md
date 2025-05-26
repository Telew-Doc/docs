# Entity

**Type:** trait  
**App:** core

**Extends:** [`RefEntity`](../core/RefEntity.md)

## Fields

### `tickets`

**Type:** `[Ticket]? read by items`

---

### `issues`

**Type:** `[IssueType[Entity]]?`

**Modifiers:** compute

---

## Functions

### `issueTypes`

**Returns:** `[IssueType]?`

**Modifiers:** back

---

### `calcIssues`

**Returns:** `[IssueType[Entity]]?`

**Modifiers:** back

---

### `activeItemType`

**Returns:** `String`

---

### `assignees`

**Returns:** `[IUser]?`

---

### `takeItem`

**Returns:** `Future[Void]`

**Modifiers:** front

---

### `itemImage`

**Returns:** `Image?`

---

### `itemRoles`

**Returns:** `[Role]?`

---

### `getItemRoles`

**Returns:** `[Role]`

---

### `itemUser`

**Returns:** `User?`

---

### `itemPriority`

**Returns:** `Dec[8]?`

---

### `itemOrder`

---

### `itemActiveOrder`

**Returns:** `NativeOrd`

---

### `at`

**Returns:** `this?`

**Modifiers:** native

---

### `revisions`

**Returns:** `[Revision[this]]?`

**Modifiers:** native

---

### `saveMain`

**Returns:** `this`

---

### `formUrl`

---

### `publicUrl`

**Returns:** `Url`

**Modifiers:** back

---

### `apiUrl`

**Returns:** `Url`

**Modifiers:** back

---

### `hasObserverInRole`

**Returns:** `Bool`

---

### `hasObserver`

**Returns:** `Bool`

---

### `isForRole`

**Returns:** `Bool`

---

### `isFor`

**Returns:** `Bool`

---

### `isForUser`

**Returns:** `Bool`

---

### `_isForUser`

**Returns:** `Bool`

**Modifiers:** back

---

### `isFor`

**Returns:** `Bool`

---

### `unreadCount`

**Returns:** `Int?`

---

### `isForCurrent`

**Returns:** `Bool`

---

### `splitPerUser`

**Returns:** `Bool`

---

### `notify`

**Returns:** `Void`

**Modifiers:** back

---

### `notifyAll`

**Returns:** `Void`

**Modifiers:** back

---

### `joinAll`

**Returns:** `[SubjectObserver]?`

**Modifiers:** back

---

## Views

### `issuesView`

---

### `dash`

---

### `fullDash`

---

### `obsView`

---

