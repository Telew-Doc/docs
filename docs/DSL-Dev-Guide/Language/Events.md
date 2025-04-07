# Events

`Events` are similar to functions but it can return only `Void` or `Future[Any]`, it cannot be overridden and all code in the hierarchy will be called.

For example, there is a system event `onSave` which is called when an entity is saved. It's declared as:

```dsl
event onSave: Future[Any] = {}
```

Then you can execute a code when an entity is saved.

```dsl
trait Foo {
    event onSave = "Foo".log
}

entity Bar extends Foo {
    event onSave = "Bar".log
}
```

If a `Bar` is saved, the both `onSave` will be called and the log will contain the both messages. Execution order is not determined.

Events are needed to make it possible event processing in the extension apps without breaking the main app. For example, if `onSave` would be a `func`, then the code for the previous example would look like:

```dsl
trait Foo {
    func onSave = "Foo".log
}

entity Bar extends Foo {
    func onSave = {
        let _ ← super.onSave
        "Bar".log
    }
}
```

It will work similarly. However what if trait `Foo` would not contain `onSave` function in the declaration but it would be declared in extension. It will not work because `super.onSave` will not be presented in the `Bar` in this case as there would not be `super.onSave` at all. It's just an example, there are another similar cases.