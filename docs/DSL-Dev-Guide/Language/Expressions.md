# Expressions

## Braces

It executes a sequence of expressions and returns the value of the latest one.

```dsl
func test = { 
    let a = 2
    let b = 3 
    a*b 
}
```

The result of the function will `a*b == 6`.

## Let

To declare an immutable variable. This variable will be visible inside braces.

## If

Conditional expression. If the condition is true it returns a positive value otherwise negative.

```dsl
if (true) 1 else 2 == 1 
if (false) 1 else 2 == 2
```

If there isn't else clause if-expression returns Option wrapped value.

```dsl
func foo: Foo = ...
func fooOpt: Foo? = if (cond) foo
```

## If Let

It allows unwrapping an optional value into a variable.

```dsl
func foo: Foo? = ...
if (let x = foo) "foo = $x" else "foo is empty"
```

If you just use a simple call to a variable or a function without parameters you can avoid letting a variable name:

```dsl
if (let foo = foo) ...
```

The same as:

```dsl
if (let foo) ...
```

You can join several let together with a comma or space. The variables declared in the previous let are available in later:

```dsl
if (let foo, let bar = foo.bar) ...
```

You can check for a condition for the variable with `where`. And you can use a condition before any variables:

```dsl
if (y < 20
    let foo where foo.x > 10
    let bar = foo.bar
) ...
```

## If Return

It allows you to check for a condition and return a value.

```dsl
if (let foo) return {
    "foo = $foo"
}
if (let bar) return "bar = $bar"
"Foo and Bar are empty"
```

It's the same as:

```dsl
if (let foo) {
    "foo = $foo"
} else if (let bar) {
    "bar = $bar"
} else {
    "Foo and Bar are empty"
}
```

## Guard

The guard expression allows decreasing indent and makes the flow flatter.

```dsl
guard (let foo) else return {
    "foo is empty"
}
guard (let bar = foo.bar) else return "bar is empty"
"foo = $foo, bar = $bar"
```

It's the same but much more readable as:

```dsl
if (let foo) {
    if (let bar = foo.bar) {
        "foo = $foo, bar = $bar"
    } else {
        "bar is empty"
    }
} else {
    "foo is empty"
}
```

## Constants

### Boolean

- `true` - Boolean true value
- `false` - Boolean false value

### Null

- `null` - Optional empty value

### This

Returns a reference to this class or you can get a reference to a parent class for inner classes:

```dsl
entity Invoice { 
    class Item { 
        func invoice: Invoice = this[Invoice] 
        func item: Item = this 
    } 
}
```