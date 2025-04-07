# Reports

Reports can show data by query. You have to provide a query for the report and you can provide a list view. List view can be auto-generated. The simplest report will look like this:

```dsl
entity Invoice { 
    field number: String
    field data: Date
    field total: Dec[2]
}

report InvoiceReport {
    view list = Invoice.all
}
```

Here the `Invoice` entity is declared for example. In `InvoiceReport` query is defined to select all invoices. You can declare a list view in the report the same way as with entity:

```dsl
report InvoiceReport {
    query = Invoice.all
    view list = Invoice.all >> table{number, date, total}
}
```

You can add the report to a menu:

```dsl
menu ReportMenu {
    report InvoiceReport
}
```

You can make any complicated layout and inline queries there. For example, you can show results of multiple queries on the same screen:

```dsl
report InvoiceReport {
    view list = column {
        Invoice.all
        Order.all
    }
}
```