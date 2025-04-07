# External Identifiers

If you need to store external identifiers, follow these steps:

1. Add dependency to `flow2b.integ`

2. Your `SystemService` should implement trait `ExtIdSource[T]` where `T` is the data type for the ID:

    ```dsl
    entity SomeIntegration extends SystemService with ExtIdSource[Int]
    ```

    It can be another entity or inline entity, but usually it will be a `SystemService`.

3. Entities or inline entities which can have external IDs should implement the `HasExtId` trait. You can extend existing entities or traits with it:

    ```dsl
    extend entity SalesOrder extends HasExtId
    ```

4. To save an external ID, you can use:

    ```dsl
    service.updateExtId(item, newExtId)
    ```

    or

    ```dsl
    item.updateExtId(service, newExtId)
    ```

5. To get an optional external ID:

    ```dsl
    service.extId(item)
    ```

    or

    ```dsl
    item.extId(service)
    ```

6. To find an item with an external ID:

    ```dsl
    service.findExtId(extIdToFind, _.as[SalesOrder])
    ```

    This will return a `SalesOrder` with the ID. The second parameter is a function which returns an optional value. It's needed to find an item of a necessary type in the case when external IDs can be the same for different types.

7. You can see external IDs for any item implementing `HasExtId` by calling the `extView` form. For this, in the URL just change `/form/` to `/extView/`.