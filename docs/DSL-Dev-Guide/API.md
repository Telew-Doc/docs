# API

## RESTful API

You can use RESTful API to get or update any entity or trait in the system.

Endpoint URL for an entity will depend on the configuration of deployed instance, more specifically on backends `apiUrl`.

!!! question "How to get this URL when developing in DSL"
    To get this URL for instance you're interested in run the following command in DSL console: `#!dsl System.apiUrl`. The output will look like similar to this: `https://wsx.tlayen.com/api/v1`.

All endpoints will begin with a structure like this:
`$BASE_API_URL/$workspaceId/$entityFullName`

!!! question "How to get entity's full name"
    Full names are visible when you visit entity's URL in some `form`, `list` or `report`. They're just a concatenation of DSL package the entity comes from + entity name (as it appears in the code) itself. To programatically get the name you can also use the following command: `#!dsl <entity>.dslType.fullName`.
    
    
    ??? note "Further explanations of `#!dsl <entity>.dslType.fullName` command" 
        If you executed this command from instanced entity (that you got in some previous step) the result should look as expected, however if you called it with an entity's `object` (just by name, e.g. `#!dsl Ticket.dslType.fullName`) it'll end with `$`, which is just an indication that the target in question is an object. You don't need to include it in endpoint URLs.


For example `GET https://wsx.tlayen.com/api/v1/73_0/flow2b.acc.finance.FinanceAccount` will return a list of all `FinanceAccount` entities inside workspace `73_0`.

The response is in JSON format, with two fields:
    1. `data` which contains ids of returned data.
    2. `map` which contains more detailed description of all used entities in the result, so not only the requested data but also data referenced in the requested data. It will have relationship id → entity data.

The list of finance accounts will look like:

```JSON
{
  "data": [
    "601_45",
    "601_6"
  ],
  "map": {
    "601_6": {
      "$av": "List",
      "id": "601_6",
      "createdOn": "2017-02-18T02:51:45.730Z",
      "createdBy": "601_2",
      "touchedOn": "2017-02-18T02:51:45.730Z",
      "legalEntity": "601_4",
      "currency": "USD",
      "balance": 1400.00,
      "name": "Bank USD"
    },
    "601_4": {
      "$av": "Ref",
      "id": "601_4",
      "title": "OAcc",
      "pricesIncludingGst": false,
      "gstStatus": "Registered"
    },
    "601_2": {
      "$av": "Ref",
      "id": "601_2",
      "name": "Anton Zherdev",
      "gstStatus": "NotRegistered"
    },
    "601_45": {
      "$av": "List",
      "id": "601_45",
      "createdOn": "2017-02-25T21:59:41.651Z",
      "createdBy": "601_2",
      "touchedOn": "2017-02-25T21:59:41.651Z",
      "legalEntity": "601_4",
      "currency": "EUR",
      "balance": 20.00,
      "name": "Bank EUR"
    }
  }
}
```

So it contains two accounts in the result with ids `601_45` and `601_6`. The data for the accounts are in the map as well as other related entities. Such structure allows to mention every entity only once even if it's used few times and serialise recursive structures.

A special field `$av` contains availability for the entity.

!!! note "TODO: Document availability structure"


### Endpoints

All prefixed by the aforementioned URL:
`API_URL = $BASE_API_URL/$workspaceId}/$entityFullName`

- `GET $API_URL`: will return all items for the entity with availability `List`
- `GET $API_URL/$id` - will return the item id with availability `All`
- `POST $API_URL` - create a new item for the entity. If `id` field is presented in the body, it will work the same as `PATCH $API_URL/$id`
- `PATCH $API_URL/$id` - update the item. Only updated fields may be presented, other fields can be omitted
- `DELETE $API_URL/$id` - delete the item


## Authentication

You can call API without authentication, but it will only have access to publicly availble data and will use the `Public Service` and its user for activities.

If you need higher level of access you'll need to create an `API Service`, it will generate API key and secret. You can assign a necessary role to the service. Then you can use [Basic Auth](https://en.wikipedia.org/wiki/Basic_access_authentication) with the key as user name and the secret as a password.

!!! warning 
    You can use a real user name and password for API access but it's a bad practice as it will not be clear that it has been done using API.


## Call functions using API

You can call some functions using API calls and it will return the result of the function in the similar way as described in [RESTful API](#restful-api) section.

It will translate the request to the function name and parameters. It's the same endpoint as for RESTful API, in fact RESTful API is just calling the functions according to the convention.

- This will call an object function for the type: `$API_URL/$workspaceId/$typeFullName/$functionName`
- This will call an instance function for the entity with id: `$API_URL/$workspaceId/$entityFullName/$id/$functionName`

!!! warning "Naming requirements"
    There's a strict naming rule when it comes to defining such callable functions in DSL.
    The function must start with the lowercase REST method (`get`, `post` etc) and then PascalCase function name:

    - getAccountData
    - postTransaction

    When calling those functions you omit the REST method and lower its first letter:

    - `GET $API_URL/$workspace_id/$typeFullName/accountData`
    - `POST $API_URL/$workspace_id/$typeFullName/transaction`



If you need to process body in the function, the request can have body as a parameter. It can be of any type and it will try to parse body in the data type.

If you want to get headers, use `headers: [String -> String]?` as a parameter.
To get all parameters, use `params: [String -> String]?`.
To get the full http request, use `request: IncomingHttpRequest`.
You can add parameters in the URL, then it will call the function with the parameters. Again it will try to parse it in a given data type.

### Examples

- `GET $BASE_API_URL/13_1000/foo.Foo/test`  
    This will call an `object func getTest` from `Foo` entity from `foo` package inside workspace `13_1000`

- `GET $BASE_API_URL/13_1000/foo.Foo/56_321/test`  
    This will call a `func getTest` from the instance with id `56_321` of entity `Foo` from package `foo` inside workspace `13_1000`

- `GET $BASE_API_URL/13_1000/foo.Foo`  
    This will call `object func get` from ... *(same as before)*. If the target is an entity, that function is already implemented and it will return all items for the entity.

- `GET $BASE_API_URL/13_1000/foo.Foo/foo/bar`  
    This will call `object func getFooBar` from ... *(same as before)*.

    !!! note "How the nested URL results in single function call"

- `GET $BASE_API_URL/13_1000/foo.Foo/test?n=10,s=test`  
    This will call `object func getTest(n: Int, s: String)` from ... *(same as before)*.

- `POST $BASE_API_URL/13_1000/foo.Foo/test`  
    This will call `object func postTest(body: Bar)` if exists or just `object func postTest` if `body` is ignored from ... *(same as before)*.


## Global Endpoints

If you need to provide one URL for your app for all workspaces and then route the request to one of the workspaces, you need to implement:

```dsl
inline trait WorkspaceEndpoint[D] {
    func service: SystemService
    func keys: [String]?
    func router: WorkspaceRouter[D]
    back func process(request: HttpRequest, data: D): Future[Any]
}

interface WorkspaceRouter[D] {
    back func parse(request: HttpRequest): D
    back func keys(request: HttpRequest, data: D): [String]?
}
```

Your workspace endpoint should return a key and the same key should be extracted by the workspace router from http request.

Global endpoint URL to send requests will be: `$BASE_API_URL/$routerFullName`

### Example

```dsl
entity MailService extends SystemService with WorkspaceEndpoint[MailData] {
    func title = “Mail $domain”
    ref field domain: String
    func keys: [String]? = [domain]
    func router = MailRouter
    func service = this
    func process(request: IncomingHttpRequest, data: MailData): Future[Any] = {
        Mail(data).save
    }
}

object MailRouter extends WorkspaceRouter[MailData] {
    back func parse(request: IncomingHttpRequest): MailData = {
        request.body.as[Data]!.parseJson[MailData]
    }
    back func keys(request: IncomingHttpRequest, data: MailData): [String]? = {
        if (request.header("X-Signature”) != data.subject.hmac("secret”).sha256.hex) {
            throw “Unsigned”
        }
        (data.to('@' .. ])!.lower
    }
}

class MailData {
    field to: String
    field subject: String
    field text: Text
}

entity Mail {
    field to: String
    field subject: String
    field text: Text
    func title = subject
}
```

Here we try to import mail if it's sent to the service in JSON format.

`MailService` is added in a workspace with a domain name as a setting. Domain is a key.
`MailRouter` parses the JSON message in the `MailData` structure.
It verifies signature to make sure that the request is coming from the expected source
It extracts domain as a key.
The system will match the key and route the request into the workspace with the domain.
`MailService` will process the request, convert `MailData` to Mail entity and saves it.
If the app is `foo.mail`, then URL for the requests will be: `$BASE_API_URL/foo.mail.MailRouter`
