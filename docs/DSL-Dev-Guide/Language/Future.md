# Future

`Future` is a value which will be calculated in future but probably not ready right now. For example, when you run an http request it takes time to obtain the result.

To process the result you need to use the `map` combinator. You can use the `←` monadic sugar syntax instead which is calling `map`.

```dsl
http("test.com").get.map{result =>
    …
}
```

is the same as

```dsl
let result ← http("test.com").get
…
```

Both of these constructions return `Future`.

!!! warning
    Be careful in `if` expressions. If one of branches returns `Future`, other one should return `Future` too in most cases.