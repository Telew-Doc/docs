# Declare Menu

You can declare a menu in a layout. The menu items can open list views for an entity, report or trait.

```dsl
role SalesPersonRole {
    menu Main {
        entity Invoice 
        entity Company
        trait ActionItem
        report InvoiceReport
    }
}
```

This will create a menu section with name `Main` and items for `Invoice`, `Company`, `ActionItem` trait, and `InvoiceReport`.

You can also control what list view you want to open and customize the menu item label:

```dsl
role SalesPersonRole {
    menu MainMenu {
        entity Invoice {
            label = "Invoices"
            list = myList
        }
        entity Company 
    }
}

entity Invoice {
    object view myList = Invoice.all >> table{code}
}
```

!!! note
    The `label` parameter allows you to customize how the menu item appears to users, while the `list` parameter lets you specify which view to use when the menu item is clicked.