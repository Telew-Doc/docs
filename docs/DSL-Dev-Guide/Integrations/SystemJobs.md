# System Jobs

System jobs are used to run background tasks and make HTTP requests. A common use case is updating prices in an e-commerce system.

## Creating a System Job

To create a system job, extend the `SystemJob` class:

```dsl
class UpdatePricesJob extends SystemJob {
    impl field service: MyService
    field product: Product
    
    impl func do: Future[Any] = {
        https("example.com/api/product").oauth2(service).post(product.json)
    }
}
```

In this example:

- The job updates product information via an HTTP request
- It requires a service instance for authentication
- The `do` function contains the actual job logic

## Running a Job

To execute a job, you need to enqueue it. This can be done in response to specific events, such as when a product is modified:

```dsl
entity Product {
    // ... other fields and functions ...
    
    func onSave = {
        UpdatePricesJob(service = myService, product = this).enqueue()
    }
}
```

When a product is saved:

1. The job is automatically enqueued
2. It runs asynchronously in the background
3. The main application flow continues without waiting for the job to complete