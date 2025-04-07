# Authentication

## Basic Authentication

```dsl
https("test.com/v1/test.json")
    .basicAuth(userName, password)
    .get
```

## OAuth 2

You can authorize your system service with OAuth or OAuth2. For this you will need to implement `OAuth` or `OAuth2` trait and then authorization will be required when user will add the service.

```dsl
entity TestIntegration extends SystemService with OAuth2 {
    field title: String
    func roles: [Role]? = [Admin]
    func authAuthorizeUrl: Url = "http://brentertainment.com/oauth2/lockdin/authorize"
    func authTokenExchangeUrl: Url = "http://brentertainment.com/oauth2/lockdin/token"
    func authClientId = "demoapp"
    func authClientSecret = "demopass"
    func authScope = " "
    
    view form = nav{grid{
        title
        serviceState
        authorizeView
    }}
}
```

Then when you do HTTP requests you will need to authorize it with the service using `oauth` or `oauth2` function accordingly:

```dsl
https("test.com/v1/test.json")
    .oauth2(testIntegration)
    .get
```

Redirect URL will be:

```
https://ws.flow2b.com/api/oauth2/$(package)/$(integration)
```

For example:

```
https://ws.flow2b.com/api/oauth2/test.package/TestIntegration
```

## OAuth 1

```dsl
entity TrademeIntegration extends SystemService with OAuth {
    field title: String
    func roles: [Role]? = [Admin]
    func authTmpTokenUrl: Url = "https://secure.tmsandbox.co.nz/Oauth/RequestToken"
    func authParams = [("scope", "MyTradeMeRead,MyTradeMeWrite")].toMap
    func authAuthorizeUrl: Url = "https://secure.tmsandbox.co.nz/Oauth/Authorize"
    func authTokenExchangeUrl: Url = "https://secure.tmsandbox.co.nz/Oauth/AccessToken"
    func authConsumerKey: String = "3A53685B186A812538CF641876E8AEA7"
    func authConsumerSecret: String = "B7E1A0CED8332454AE2919AE6E836354"
}

https("api.tmsandbox.co.nz/v1/Categories.json")
    .oauth(trademeIntegration)
    .get
```