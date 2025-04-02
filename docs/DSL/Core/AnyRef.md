# AnyRef

## Overview

**Type**: trait
**Extends**: [AnyRef](AnyRef.md)


## Native Functions

### `fullTitle: String`
### `get[T](field: String): T`
### `update(field: String, value: Any): this`
### `default[R](field: this => R): NoInfer[R]`
### `defaultAllFields(): Void`
### `clear[R](field: (this) => R): NoInfer[R?]`
### `updated(field: (this) => Any): Bool`
### `origin[R](field: (this) => R): NoInfer[R]`
### `validationErrors: [String]?`
### `increment(field: this.object => Int?): Int?`
### `silentUpdate[R](field: this => R, value: NoInfer[R]): NoInfer[R]`
### `rollback: this`
### `json: Json`
### `xml: Xml`
### `toMap: [String -> Any]?`
### `dslType: DslType`


## Object Native Functions

### `dslType: DslType`