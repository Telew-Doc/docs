# Scheduled Jobs

You can run scheduled jobs with a cron scheduler syntax: https://en.wikipedia.org/wiki/Cron

**However in our case the first item is denoting seconds.**

!!! note "It's an inlined entity and should be saved usually along with service."

```dsl
entity HelloService {
    field title: String
    field job: HelloJob inline by service
}

inline entity HelloJob extends ScheduledJob {
    field service: HelloService by job
    func schedule = "0 0 * * * ?" //Every hour
    func do: Future[Any] = {
        let hello = Discussion(title = "Hello").save
        Person.all.filter(login).foreach{person => 
            person.join(hello).notify()
        }
    }
}
```

!!! tip "To disable the job you can return an empty string as a schedule."