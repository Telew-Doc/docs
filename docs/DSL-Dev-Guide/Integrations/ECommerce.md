# E-Commerce Integration

## Service

You need to do:

1. Add dependency to `flow2b.integ.ecom`

2. Implement trait `ECommerceIntegration[ID]` where `ID` is the data type for external identifier. This will be your service:

    ```dsl
    entity WooCommerceIntegration extends ECommerceIntegration[Int]
    ```

3. Add necessary settings for your e-commerce platform and implement `mainView` which will contain the settings:

    ```dsl
    ref field url: Url
    field consumerKey: String
    field consumerSecret: Password  
    
    view mainView = grid(labels = Top) {
        url
        consumerKey
        consumerSecret
    }
    ```

## Products

1. Implement `updateProductJobs` which will upload products to e-commerce:

    ```dsl
    func updateProductJobs(change: BatchChange[ProductUpdate[ICustomerSuperProduct]]): [SystemJob]? = {
        [UpdateProductsJob(service = this, change = change)]
    }
    ```

    The `BatchChange` contains one or few products which were created, updated, or deleted.
    If your e-commerce supports batch operations, you should use it and send all updates in one or few batches. If it does not support batch operations, you can create separate jobs for every product and operation.

    In order to save external IDs for newly created products for the batch update, you can use `updateExtIds` of `BatchChange`:

    ```dsl
    change.updateExtIds(service, response.createdItems.map(id))
    ```

2. If the e-commerce supports categories, similarly implement `updateCategoryJobs`:

    ```dsl
    func updateCategoryJobs(change: BatchChange[ProductCategory]): [SystemJob]?
    ```

    Categories will be separated into batches in such a way that parent categories would be created in the previous batch.
    Categories will be created before products.

3. If the e-commerce supports brands, similarly implement `updateBrandJobs`:

    ```dsl
    func updateBrandJobs(change: BatchChange[Brand]): [SystemJob]?
    ```

4. If the e-commerce supports variations, you need to implement:

    ```dsl
    func updateAttrJobs(change: BatchChange[ProductAttr]): [SystemJob]?
    func updateAttrTermJobs(change: BatchChange[ProductAttrTerm]): [SystemJob]?
    func updateVariationJobs(change: BatchChange[ProductUpdate[ICustomerComplexProduct]]): [SystemJob]?
    ```

    - `updateAttrJobs` updates attributes (e.g., color)
    - `updateAttrTermJobs` updates attribute terms (e.g., orange color, green color, etc.). This function will be called after `updateAttrJobs`
    - `updateVariationJobs` updates product variations, creating combinations of products and attributes (e.g., green cup, orange cup, green plate). This function will be called after `updateAttrJobs`, `updateAttrTermJobs`, and `updateProductJobs`

## Customer

1. To download customers, create a model for the customer data for e-commerce and implement trait `ECustomer[ID]`:

    ```dsl
    back class CustomerData extends ECustomer[Int] {
        extFieldNaming = Underscore
        field id: Int
        field email: String
        field firstName: String?
        field lastName: String?
        field username: String?
        field billing: WooAddress?
        field shipping: WooAddress?
        
        func extId = id
        func personFullName: String? = "$firstName $lastName".trim.or(username)
        func emails = [email]
        func phones = []
        func billingAddresses = billing.toSeq
        func deliveryAddresses = shipping.toSeq
    }
    ```

2. Implement `func downloadCustomersJobs: [SystemJob]?` which will return the job to download all customers. This function will be called initially or when settings are changed.

3. In the job, parse e-commerce response into the model and call `make(service)` function which will create customers in the system:

    ```dsl
    back class DownloadCustomersJob extends SystemJob {
        field service: WooCommerceIntegration
        
        func do: Future[Any] = {
            procPage(1)
        }
        
        func procPage(page: UInt): Future[Void] = {
            let response <- service.https("/customers")
                .param("page", page)
                .param("per_page", "10")
                .get
            let customers = response.body!.parseJson[[CustomerData]?]
            customers*.make(service)
            if (customers.count == 10) {
                procPage(page + 1)
            }
        }
    }
    ```

4. Register a webhook in e-commerce and create customers on the webhooks.

    If you need to register webhooks automatically to a callback URL, use:

    ```dsl
    func createWebhookJobs: [SystemJob]?
    ```

    If you have to set a static URL, please follow #Article: Global Endpoint

## Order

1. Create a model for order and implement `ESalesOrder[ID]`

2. Implement:

    ```dsl
    func downloadOrdersJobs(from: Date?): [SystemJob]?
    ```

    `from` is a date after which you need to download orders.

3. In the job, before you import orders, call `service.ordersDownloaded(now)`. This will save the date for the next time and then download data and call `make(service)` for all orders:

    ```dsl
    back class DownloadOrdersJob extends SystemJob {
        field service: WooCommerceIntegration
        field from: Date?
        
        func do: Future[Any] = {
            service.ordersDownloaded(now)
            procPage(1)
        }
        
        func procPage(page: UInt): Future[Void] = {
            let req = service.https("/orders")
                .param("page", page)
                .param("per_page", "10")
            if (let from) req.param("after", from.format("yyyy-MM-dd'T'HH:mm:ss"))
            let response <- req.get
            let orders = response.body!.parseJson[[OrderData]?]
            let _ <- orders*.make(service).allCompleted
            if (orders.count == 10) {
                procPage(page + 1)
            }
        }
    }
    ```

4. Register a webhook in e-commerce and create customers on the webhooks. Usually, you will be able to use the same infrastructure as for customers.

    If you need to register webhooks automatically to a callback URL, use:

    ```dsl
    func createWebhookJobs: [SystemJob]?
    ```

    If you have to set a static URL, please follow #Article: Global Endpoint

5. In order to update order state in e-commerce when the order is marked as delivered or paid in the system, implement:

    ```dsl
    func uploadOrderStateJobs(orders: [SalesOrder]): [SystemJob]?
    ```

    You will need to update the order state in the e-commerce based on the order fields, status, deliveryState, and paymentState.
