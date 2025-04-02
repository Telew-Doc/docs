# DSL DB

## App class

### Properties

| # | NAME        | LINKED-TYPE/CLASS | MANDATORY | READONLY | NOT-NULL |
|---|-------------|-------------------|-----------|----------|----------|
| 0 | owner       | STRING            | true      | false    | false    |
| 1 | dslPackage  | STRING            | true      | false    | false    |
| 2 | versions    | [RID]             | false     | false    | false    |
| 3 | mng         | STRING            | true      | false    | false    |
| 4 | name        | STRING            | false     | false    | false    |
| 5 | description | STRING            | false     | false    | false    |
| 6 | uuid        | UUID              | true      | false    | false    |
 
> `dslPackage` represents the app name (used in dependencies, URLs and DSL class names in DB),  
> while `name` represents human-readable app name for UI and isn't required to be set.
> 
> `versions` lists all `AppSource` records with this app
> 
> `owner` determines under which workspace the app will be listed (in system admin dashboard).  
> `mng` determines which workspace will receive generated error messages from this app.  
> Both `owner` and `mng` workspaces allow for app modifications within them (for all other workspaces it's in read-only mode).
> 
> `description` only for UI, 🚧 TODO: `uuid` purpose unknown.

### Indexes

| # | NAME           | PROPERTIES   | TYPE      |
|---|----------------|--------------|-----------|
| 0 | App.dslPackage | [dslPackage] | UNIQUE    |
| 1 | App.mng        | [mng]        | NOTUNIQUE |
| 2 | App.owner      | [owner]      | NOTUNIQUE |

## AppSource class

### Properties

| # | NAME         | LINKED-TYPE/CLASS | MANDATORY | READONLY | NOT-NULL | MIN | MAX | COLLATE | DEFAULT |
|---|--------------|-------------------|-----------|----------|----------|-----|-----|---------|---------|
| 0 | app          | RID               | true      | false    | false    |     |     | default |         |
| 1 | dslPackage   | STRING            | true      | false    | false    |     |     | default |         |
| 2 | releaseNotes | STRING            | false     | false    | false    |     |     | default |         |
| 3 | files        | [OBJECT]          | false     | false    | false    |     |     | default |         |
| 4 | touchedOn    | DATE              | true      | false    | false    |     |     | default |         |
| 5 | uuid         | UUID              | true      | false    | false    |     |     | default |         |
| 6 | version      | STRING            | true      | false    | false    |     |     | default |         |
| 7 | dependencies | [OBJECT]          | false     | false    | false    |     |     | default |         |

> ⚠️ Technically not a property but `status` field is set for every document  
> indicating which dev channel the app is on: Prod, Beta, Cancelled etc.
> 
> `app` links this version to the `App` record. `dslPackage` duplicates this apps name (`App.dslPackage`).
> 
> `releaseNotes` is for the corresponding UI field. `touchedOn` last update date. 🚧 TODO: `uuid` purpose unknown.
> 
> `version` formatted as `<number>.<number>.<number>`, e.g. `1.0.0`, `5.41.4` etc.
> 
> `files` stores array of objects of structure: `{ name: <STRING DSL <<FILE>> NAME>, content: <STRING DSL <<FILE>> CONTENT> }`.  
> Files are just visual representations in UI when you edit code in the browser (although our export / import tools also separate those into separate system files).
> 
> `dependencies` represents an array of dependencies for this app version, uses objects of structure:  
> { dslPackage: <CORRESPONDING App.dslPackage DSL APP NAME>, channelRange: <VERSION RANGE + CHANNEL INFO, E.G. [2.0.0:4.0.0):Prod> }

## Queries

- `select from App`

| #  | @RID   | @CLASS | owner | dslPackage   | versions | mng   | uuid                                    | name | description |
|----|--------|--------|-------|--------------|----------|-------|-----------------------------------------|------|-------------|
| 0  | #14:0  | App    | core  | inventory    | [#12:0]  | core  | 301898890866894320827068252999597835690 |      |             |
| 1  | #14:1  | App    | 13_1  | w13_1        | [#12:1]  | 13_1  | 205964616463186809103591753990785401249 |      |             |
| 2  | #14:2  | App    | 13_8  | w13_8        | [#12:2]  | 13_8  | 224436480461500118092711859861186299895 |      |             |
| 3  | #14:3  | App    |       | w13_9        | [#12:3]  |       | 293067100589035669072796268629798179421 |      |             |
| 4  | #14:4  | App    | 13_13 | w13_13       | [#12:4]  | 13_13 | 127009406275926576603515627651522476461 |      |             |
| 5  | #14:5  | App    |       | w13_14       | [#12:5]  |       | 12595021365579212540036805690848954976  |      |             |
| 6  | #14:6  | App    |       | w13_16       | [#12:6]  |       | 176034495396410854800586560472177104602 |      |             |
| 7  | #14:7  | App    |       | w13_17       | [#12:7]  |       | 214862792873557138558749684635777510330 |      |             |
| 8  | #14:8  | App    |       | w13_21       | [#12:8]  |       | 248176687705240463487547267265393795555 |      |             |
| 9  | #14:9  | App    |       | w13_36       | [#12:9]  |       | 137821365172037241554447820236214208728 |      |             |
| 10 | #14:10 | App    | 13_40 | w13_40       | [#12:10] | 13_40 | 172748718596863642921406112439751691788 |      |             |
| 11 | #14:11 | App    |       | w13_57       | [#12:11] |       | 137335442470786545504768165718439949855 |      |             |
| 12 | #14:12 | App    | 13_73 | w13_73       | [#12:12] | 13_73 | 58395530132835021905800778058806388514  |      |             |
| 13 | #14:13 | App    |       | w13_75       | [#12:13] |       | 24572296635373917220293448933338634505  |      |             |
| 14 | #14:14 | App    | 13_76 | w13_76       | []       | 13_76 | 239003100296143018996045752092594075809 |      |             |
| 15 | #14:15 | App    | 13_78 | w13_78       | [#12:14] | 13_78 | 167012136330673499418302600632909396675 |      |             |
| 16 | #14:16 | App    | 13_79 | w13_79       | [#12:15] | 13_79 | 307708543891116902439305550754166715539 |      |             |
| 17 | #14:17 | App    | 13_79 | zherdev.prod | [#12:16] | 13_79 | 48343246190824829736409558743711998752  |      |             |
| 18 | #14:18 | App    | 13_78 | zherdev.cafe | [#12:17] | 13_78 | 156666957942852638362158320754085611876 |      |             |
| 19 | #14:19 | App    | 13_82 | w13_82       | [#12:18] | 13_82 | 2177527482051362747741086043963149354   |      |             |


- `select from AppSource`

| #  | @RID   | @CLASS    | owner | app    | version | status | dslPackage | releaseNo | touchedOn | uuid      | dependencies | files                                                                     |
|----|--------|-----------|-------|--------|---------|--------|------------|-----------|-----------|-----------|--------------|---------------------------------------------------------------------------|
| 0  | #12:0  | AppSource | core  | #14:0  | 1.0.0   |        | inventory  |           | 2017-0... | 100708... | []           | [{name:Invoice,content:entity Invoice { ref field number: String r...     |
| 1  | #12:1  | AppSource | 13_1  | #14:1  | 1.0.0   | Prod   | w13_1      |           | 2020-0... | 949854... | [{dslP...    | []                                                                        |
| 2  | #12:2  | AppSource | 13_8  | #14:2  | 1.0.0   | Prod   | w13_8      |           | 2020-0... | 247353... | [{dslP...    | []                                                                        |
| 3  | #12:3  | AppSource |       | #14:3  | 1.0.0   |        | w13_9      |           | 2017-0... | 314465... | []           | [{name:Relationships.erp,content: entity Role {field title: String ...    |
| 4  | #12:4  | AppSource | 13_13 | #14:4  | 1.0.0   | Prod   | w13_13     |           | 2019-0... | 181953... | [{dslP...    | [{name:Resources.erp,content:entity Resources{ field title : String ...   |
| 5  | #12:5  | AppSource |       | #14:5  | 1.0.0   |        | w13_14     |           | 2017-0... | 923866... | []           | [{name:access, menu.erp,content:role Marketing{ entity Content } },...    |
| 6  | #12:6  | AppSource |       | #14:6  | 1.0.0   |        | w13_16     |           | 2017-0... | 112219... | []           | [{name:enums.erp,content:enum PlanningType{ case Goal case Challen...     |
| 7  | #12:7  | AppSource |       | #14:7  | 1.0.0   |        | w13_17     |           | 2017-0... | 250610... | []           | [{name:ActionItem,content:// Something that requiers an action from th... |
| 8  | #12:8  | AppSource |       | #14:8  | 1.0.0   |        | w13_21     |           | 2017-0... | 130918... | []           | []                                                                        |
| 9  | #12:9  | AppSource |       | #14:9  | 1.0.0   |        | w13_36     |           | 2017-0... | 950889... | []           | []                                                                        |
| 10 | #12:10 | AppSource | 13_40 | #14:10 | 1.0.0   | Prod   | w13_40     |           | 2020-0... | 327253... | [{dslP...    | [{name:SavouryPotWeb,content:entity SavouryPotSupportedWebSite { fie...   |
| 11 | #12:11 | AppSource |       | #14:11 | 1.0.0   |        | w13_57     |           | 2017-0... | 722456... | []           | [{name:Transaction,content:entity Transaction { field date: Date = n...   |
| 12 | #12:12 | AppSource | 13_73 | #14:12 | 1.0.0   |        | w13_73     |           | 2017-0... | 227558... | [{dslP...    | [{name:NewFile.erp,content:entity Company { field code: Int field ...     |
| 13 | #12:13 | AppSource |       | #14:13 | 1.0.0   |        | w13_75     |           | 2017-0... | 129951... | []           | [{name:NewFile.erp,content:entity Company { field code: Int field ...     |
| 14 | #12:14 | AppSource | 13_78 | #14:15 | 1.0.0   |        | w13_78     |           | 2017-0... | 602729... | [{dslP...    | [{name:Product,content:/*entity Product { field title: String fiel...     |
| 15 | #12:15 | AppSource | 13_79 | #14:16 | 1.0.0   |        | w13_79     |           | 2017-0... | 605565... | [{dslP...    | []                                                                        |
| 16 | #12:16 | AppSource | 13_79 | #14:17 | 1.0.0   |        | zherde...  |           | 2017-0... | 124786... | []           | []                                                                        |
| 17 | #12:17 | AppSource | 13_78 | #14:18 | 1.0.0   | Prod   | zherde...  |           | 2017-0... | 927067... | []           | [{name:Unit,content:entity Unit { width = 0.08 field shortName:...        |
| 18 | #12:18 | AppSource | 13_82 | #14:19 | 1.0.0   |        | w13_82     |           | 2017-0... | 134101... | []           | []                                                                        |
| 19 | #12:19 | AppSource | 13_80 | #14:20 | 1.0.0   |        | w13_80     |           | 2017-0... | 186320... | []           | []                                                                        |

### Export

```text
export database dsldb.json -includeSecurity=false
```

### Import

```text
import database dsldb.json.gz -preserveClusterIDs=true -deleteRIDMapping=false
```

> ⚠️ By default this will overwrite the current data. To merge you must specify the `-merge` option.

You then need to make sure that the main workspace is the manager & owner of the correct Apps:

```text
update App set mng = '57_0' where mng = '13_1'
update App set owner = '57_0' where owner = '13_1'
```
