# Automation

In DSL you can create, modify, delete entities or show them to user. You can declare the code for example as a button action.

```dsl
button("Create new company") {
    Company(title = "New company", code = "New code").save
}
```

This code will create a new company with values set for the title and code fields and save it in the database. It will not be displayed to the user. In order to display it to the user you can use the following code.

```dsl
button("Create new company") {
    Company(title = "New company", code = "New code").form.open
}
```

It will show the form to user and will not save it into database until user's action. You can display form for existing entity by the same way.

You can modify existing entities. In order to save changes into database you must call the `save` function. Otherwise these changes will happen only on the user's screen.

```dsl
company.title = "Modified title"
company.save
```

You can also delete an existing entity by calling the `delete` function. It will be deleted from database.

```dsl
company.delete
```