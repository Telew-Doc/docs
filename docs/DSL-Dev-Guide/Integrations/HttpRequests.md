# HTTP Requests

You can make HTTP or HTTPS requests in the jobs. This will execute GET request and will return a `Future` with `HttpResponse`.

```dsl
let response ← https("www.test.com/api/something").get
if (response.code == 200) {
    let foo: Foo = response.data!.parseJson[Foo]
}
```

Response will contain code, headers and body.

## Parameters

You can add parameters to your request with `param` or `params` functions:

```dsl
http("test.com/product")
    .param("id", 10)
    .param("user", "test")
    .get
```

It's the same as:

```dsl
http("test.com/product")
    .params(["id" → 10, "user" → "test"])
    .get
```

Or a class can be used:

```dsl
class Foo {
    field id: Int
    field user: String
}

http("test.com/product")
    .params(Foo(id = 10, user = "test"))
    .get
```

## Headers

If you need additional header use `header` or `headers` function:

```dsl
http("test.com/product/updateTitle")
    .header("Authorization", "Key")
    .header("accept", "image/*")
    .post("Test")
```

It's the same as:

```dsl
http("test.com/product/updateTitle")
    .headers(["Authorization" → "Key", "accept" → "image/*"])
    .post("Test")
```

## Send Data

To post, put or patch some data use corresponding function with the parameter:

```dsl
http("test.com/product/updateTitle")
    .post("Some data")
```

You can serialize a class using #Article: Serialization:

```dsl
class Foo {
    field id: Int
    field title: String
}

http("test.com/product/updateTitle")
    .post(Foo(id = 10, title = "Test").json)
```

## Post Encoded Form

You can post a URL encoded form with the `form` method:

```dsl
class Foo {
    field id: Int
    field title: String
}

http("test.com/product/updateTitle")
    .form(Foo(id = 10, title = "Test"))
    .post
```

A map can be used as well:

```dsl
http("test.com/product/updateTitle")
    .form(["id" → "10", "title" → "Test"])
    .post
```