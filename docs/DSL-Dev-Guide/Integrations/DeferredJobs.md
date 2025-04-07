# Deferred Jobs

If you do not have a schedule but have a particular time when it should be triggered you can use deferred jobs. To disable the job you need to return `null` as `jobDate`.

```dsl
entity Opportunity extends Todo with DeferredJob {
    // ... other fields and functions ...
    field owner: Person?
    field nextContact: Date?
    field service: MyService
    
    func jobDate = contactAgain
    
    func do = {
        owner?.join(this)?.notify()
        nextContact = null
        save()
    }
}
```