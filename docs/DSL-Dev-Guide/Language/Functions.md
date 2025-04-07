# Functions

Functions can take parameters. A function without parameters is almost the same as compute field but the result will not be shown to the user by default and you cannot make it editable.

```dsl
entity Foo {
  func add(x: Int, y: Int): Int = x + y
  field bar = add(2, 3) // 2 + 3 = 5
}
```

It's not necessary to explicitly enter a result data type. It can be inferred automatically:

```dsl
func add(x: Int, y: Int) = x + y
```

!!! danger
    In rare cases, particularly when working with `Query` and `Future` results, implicit type conversions can lead to unexpected results. To avoid this, it's recommended to explicitly specify the return type.

You can call function and pass parameters by the position as in the example or you can specify the name of the parameter so to make code more readable in some cases. All the examples will give the same result 5:

```dsl
add(x = 2, y = 3) 
add(x = 2, 3)
add(2, y = 3) 
add(2, 3)
```

Unlike many other languages, there is no return statement. All expressions return value and this value will be used as a result of the function. If you have a sequence of instructions in your function the result of the last instruction will be the result of the function. You can use braces to achieve it:

```dsl
func foo = {
  let x = 2
  x*x
}
foo == 4
```