# Logging and Tracing

While there is no debugger available for DSL, you can use logging and tracing functions to inspect values during execution.

## Logging

The `log` function allows you to print values to the console:

```dsl
foo.log
```

This will print the value of `foo`. The output will be visible in:
- JavaScript console (when triggered from the client)
- Service activities (when executed on the server)

You can also add a label to the log output:

```dsl
foo.log("label")
```

This will print: `label = <value>`

## Tracing

The `trace` function is useful for debugging expressions. It prints both the expression and its value:

```dsl
(foo + 1).trace
```

This will print: `foo + 1 = <value>`

You can also add a label to trace output:

```dsl
foo.trace("label")
```

This will print: `label: foo = <value>`

## Chaining

Both `log` and `trace` functions return the original value, allowing you to chain them with other operations:

```dsl
foo.trace.bar.log("bar").baz
```

This makes it easy to inspect values at different points in a chain of operations.