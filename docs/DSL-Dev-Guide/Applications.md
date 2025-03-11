# Applications

To get list of application for a workspace in the menu press `Admin / Apps`. 
You will see the apps loaded by the current workspace.
If you have `Admin` priveleges in the workspace you can go to the `System Admin` dashboard and see apps that are owned by this workspace. Ownership allows for app modifications and deletions, while other workspaces only allow reading. There's also a concept of manager workspace, which means that this workspace will receive all auto-generated app issues and will also have rights to modify the app.


## Workspace App

Every workspace has its own workspace app. This app will contain dependencies for other installed applications and can contain some code specific for this workspace only.

This app cannot be deleted or used in another workspaces. It can only have one version.

!!! danger
    You can still technically create mutliple versions, and I've seen it being the case in some older workspaces, but it's not advisable to do so as the results are unpredictable and support is limited.

When you need to install an app into workspace you simply need to add dependency into the workspace app.


## App

Every app should have a unique package name. The name will be used to set dependencies and install apps.

The app package name is a dot-separated string. It should start with your company identifier to avoid package name clash. You can use your website domain as the identifier. Then it should contain identifier for the app. For example, `com.telew.crm`.

If the solution is complex and has more than one app, it can have longer package names. For example, `com.telew.inventory.stock` and `com.telew.inventory.order`. In this case, the base package is `com.telew.inventory`; `stock` and `order` are sub-packages.

!!! note
    As far as I know there's no real difference in how you organize the apps, this hierarchy is used only for manual app imports / exports but those are not relevant for DSL devs and for common users.

App title and description are not used anywhere currently. In future, a user will see the title and description in the app store.


## App Dependencies

If one app is dependant on another, it can use and extend the entities and another declared types of the second app.

You can add dependency in settings of the app version. You need to enter package name and you can also limit dependency to a particular version or version range. For example, *[2.0.0, 3.0.0)* means from *2.0.0* including to *3.0.0* excluding. Square bracket means including, round bracket excluding.


## App Versioning

You can have few versions of the same app. Versions have its state:

- *Production*: any workspace can use this version
- *Development*: this version will not be used by any other workspace except the workspace which owns the app or if the version is set exactly in the dependancy.
- *Canceled* - version is not available for any workspace.

!!! notes
    TODO: No mention of *Alpha* / *Beta* / etc versions, curios if there's any functional differences between them or it's all just *Development* version with extra labels.

For example, you can have *1.0.0* which is in *Production*, and *2.0.0* in *Development*. It means all workspaces which installed the app will have *1.0.0* except the workspace owning the app. However, you can force installation *2.0.0* in another workspace if you set this version in the dependency explicitly. It can be helpful for beta testing.

There are three numbers in the version:

- *Major*: it should be incremented when API is changed and dependant apps can be broken.
- *Minor*: it should be incremented when some new functionality has been added or existing functionality has been modified.
- *Patch*: it should be incremented when bugs have been fixed in the app.


## Sandbox Workspaces

If you develop an application, it's recommended to create a separate sandbox workspace which will contain only testing data. This will allow to not disrupt anybody and to not damage real data during development process.

You need to keep the app in development state until it's ready. When you change it to published state it will be immediately pushed into other workspaces dependant on this app version.

If data conversion is required, it should be done manually through console since there is no automatic conversion currently.

!!! note
    There's actually an automatic conversion mechanism in DSL, it can happen when app version number changes and must be manually coded in. TODO a guide for it.
