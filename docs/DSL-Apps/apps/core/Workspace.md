# Workspace

**Type:** entity  
**App:** core

## Fields

### `supportUnits`

**Type:** `Int?`

**Modifiers:** system

---

### `frozen`

**Type:** `Bool`

**Modifiers:** const

---

### `countryCode`

**Type:** `String`

---

### `timeZone`

**Type:** `String`

---

### `outsideUsersCanJoin`

**Type:** `Bool`

---

### `useLocalHelpOnly`

**Type:** `Bool`

---

### `dashboards`

**Type:** `[Dashboard]? inline by workspace`

**Modifiers:** system

---

### `apps`

**Type:** `[String -> String]?`

**Modifiers:** system

---

### `notifications`

**Type:** `[NotifyTemplate]?`

**Modifiers:** compute

---

## Functions

### `current`

**Returns:** `Workspace`

**Modifiers:** native, object

---

### `crossId`

**Returns:** `UInt?`

**Modifiers:** native, object

---

### `currentId`

**Returns:** `UInt`

**Modifiers:** native, object

---

### `getAllIds`

**Returns:** `Future[[String]?]`

**Modifiers:** native, object

---

### `getEveryWorkspaceInfo`

**Returns:** `Future[[String]?]`

**Modifiers:** native, object

---

### `canRead`

**Modifiers:** impl

---

### `canWrite`

**Modifiers:** impl

---

### `dashboard`

**Returns:** `Dashboard`

**Modifiers:** back

---

### `actor`

**Returns:** `Actor?`

---

### `apiRoot`

**Modifiers:** back

---

### `updateAppVersion`

**Returns:** `Void`

**Modifiers:** back

---

### `cleanAppVersion`

**Returns:** `Void`

**Modifiers:** back

---

### `appVersion`

**Returns:** `String?`

---

### `hasNfc`

**Returns:** `Bool`

---

## Views

### `form`

**Modifiers:** impl

---

