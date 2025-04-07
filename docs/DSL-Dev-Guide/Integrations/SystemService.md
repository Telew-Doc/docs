# System Service

A system service is required when you need to:
- Create integrations
- Run scheduled jobs
- Make HTTP requests

To create a system service, define an entity that extends `SystemService`:

```dsl
entity MyIntegration extends SystemService { 
    impl func title: String = "My Integration"
    impl func roles: [Role]? = [InventoryManager] 
}
```

## Access Control

A system service operates as a user within the system and requires appropriate role assignments to access data. While the `Admin` role provides full access, it's recommended to assign specific roles with limited permissions for better security.

## Service States

A system service can be in one of several states:

- **Active**: The service is running normally
- **Error**: An error has occurred
- **Disabled**: Too many errors have occurred and the service has been stopped
- **Inactive**: The service has been manually disabled

The service is operational only when in `Active` or `Error` state. You can disable a service by setting its state to `Inactive`.

## Error Handling

When an error occurs:

1. The service state automatically changes to `Error`
2. All admin users receive notifications about the error

After fixing the error:

1. Set the state back to `Active`
2. Keep the error notification for reference
3. This allows you to track successful operations while maintaining visibility of past issues