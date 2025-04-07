# Local Variables

You can declare a local immutable local variable. It can be useful to keep there a calculation result which will be used in a few places or to make the code more readable.

```dsl
let x = 2 
x*x == 4
```

!!! note "You *cannot* assign a new value to x."

To declare a mutable variable, use the `var` keyword:

```dsl
var x = 2
x == 2
x = x*2
x == 4
```