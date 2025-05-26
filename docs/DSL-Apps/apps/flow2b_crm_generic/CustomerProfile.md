# CustomerProfile

**Type:** entity  
**App:** flow2b.crm.generic

## Fields

### `sGender`

**Type:** `Gender?`

---

### `gender`

**Type:** `Gender?`

**Modifiers:** compute

---

### `sAge`

**Type:** `ProfileAge?`

---

### `age`

**Type:** `ProfileAge?`

**Modifiers:** compute

---

### `sIncome`

**Type:** `ProfileIncome?`

---

### `income`

**Type:** `ProfileIncome?`

**Modifiers:** compute

---

### `sLocation`

**Type:** `Address?`

---

### `location`

**Type:** `Address?`

**Modifiers:** compute

---

### `description`

**Type:** `Text?`

---

### `superProfiles`

**Type:** `[CustomerProfile]? by subProrifiles`

---

### `subProrifiles`

**Type:** `[CustomerProfile]? read by superProfiles`

---

## Views

### `form`

**Modifiers:** impl

---

