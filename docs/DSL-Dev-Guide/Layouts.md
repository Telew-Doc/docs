# Layouts

## Navigation

**`nav`** layout creates:

- Navigation bar
- Filters panel for a list view
- Activities panel with comments for a form

```dsl
entity Company {
    field title: String
    view form = nav { 
        grid {
            title
        }
    }
}
```

!!! warning "Without `nav` you will get only a grid without navigation bar and comments"


## Table

**`table`** shows field labels in header and then rows for every item. Usually it is only used to show many items as a list view or to show collection fields.

```dsl
entity Company {
    field code: Int
    field name: String
    object view list = Company.all >> nav {
        table { code, name }
    }
}
```

You can use it inside a form as well:

```dsl
entity Invoice {
    field number
    field items: [InvoiceItem] inline
    view form = nav {
        column {
            grid { number }
            items >> table { product, qty }
        }
    }
}

entity InvoiceItem {
    field product: Product
    field qty: Dec[2]
}
```


## List

**`list`** layout allows to replicate any other layouts and show collection field.

```dsl
entity Invoice {
    field number: String
    field data: Date
    field items: [InvoiceItem] inline
    view form = column {
        grid {
            number
            date
            items >> list {
                grid(labelsAlignment = Top) { product, qty }
            }
        }
    }
}

entity InvoiceItem {
    field product: Product
    field qty: Dec[2]
}
```


## Grid

**`grid`** layout shows fields with labels. First of all, it determines the most convenient for reading text column width depending on the maximum available width for the layout and desirable amount of text columns for the grid. You can set amount of text columns using the width modifier. By default it's 1.0 but it can make sense to make it higher for multicolumn forms.

```dsl
entity Company {
    field code: Int
    field name: String
    field description: String
    impl view form = grid {
        code
        name
        description
    }
}
```

The grid layout can decrease or increase the font size ensuring the best user experience for his screen size. If screen size is too small it can break multicolumn form and convert it into one column.

To create a multicolumn form you have to use the row sublayout. In this case labels will be on the top because it's recommended way from user experience perspective.

```dsl
entity Company {
    field code: Int
    field name: String
    field description: String
    impl view form = grid {
        row { code, name }
        description
    }
}
```

Row will show few fields on the same row. By default all fields will have the same width. You can modify it using the width modifier. It measures width in text columns as well as grid layout. The sum of widths of fields in a row should not be higher than the grid's width.

```dsl
entity Company {
    field code: Int
    field name: String
    field description: String
    impl view form = grid {
        row { code >> field(width = 0.3), name >> field(width = 0.7) }
        description
    }
}
```


If you need to create a free space in the form, you can use the `space` sublayout.

```dsl
entity Company {
    field code: Int
    field name: String
    field description: String
    impl view form = grid {
        row {
            space(width = 0.4),
            code >> field(width = 0.3),
            name >> field(width = 0.3)
        }
        description
    }
}
```

## Columns & Rows

Self-explanatory, can be referenced in code as `column` / `row` or `y` / `x` respectivelly.

!!! danger "There are some front-end bugs involving `column` / `row` layouts specifically, prefer `y` / `x`"

```dsl
entity Company {
    field status: Status
    field code: Int
    field name: String
    field description: String
    impl view form = grid {
        x { status code }
        y { name description }
    }
}
```

## Fields

When you use an expression as a layout by default the `field` layout will be used.
This means that you will need to use this layout explicitly only if you want to provide some modifiers.

```dsl
entity Company {
    field code: Int
    field name: String
    field description: String
    impl view form = grid {
        x { code, name }
        description >> field(span = 2)
    }
}
```

`code` and `name` are also field here but we do not want to set any modifiers for those fields. But we want to set the `span` modifier to `2` for the `description` field so that it would span all two columns of our grid.


## Labels and Headers

`label` is a static text that user cannot modify. You can also create a header using `h1`, `h2` or `h3`.

```dsl
entity Company {
    field code: Int
    field name: String
    field description: String
    impl view form = y {
        h2("Main fields")
        grid { code, name }
        label("Some description about form")
    }
}
```

## Buttons

You can use `button`s to trigger some custom action when user press them.

```dsl
entity Company {
    field code: Int
    field name: String
    impl view form = y {
        grid { code name }
        button("Update name & Code") {
            code = 1
            name = "Test"
        }
    }
}
```

`button("Update name & Code")` created a button with title `"Update name & Code"`. This is a shorter form of `button(label = "Update name & Code")`. If you want to add some more modifiers you can simply write `button("Update name & Code", span = 2)`.

Inside braces there is an action script which will be executed when user presses the button. In this example, we set code field to `1` and name to `"Test"`.

!!! warning "Running back-end code with `button`s"
    Sometimes you'd want to run a back-end job or trigger some back-end function on button press.
    You won't be able to do this normally with the code above, but if you wrap your back-end code in `!#dsl back { ... }`
    you'll be able to circumvent this. E.g.:
    ```dsl
    ...
    button("Run back-end job") {
        back {
            SomeJob(...).enqueue()
        }
    }
    ...
    ```


## Styles

!!! danger "This is literally never used, I'd be surprised if this even works"

There two ways how to set colors, fonts and other styles to your component:
- CSS modifier
- Style declaration and modifier

Both ways will use CSS. You can use the CSS reference to find out what options are available.

### CSS modifier

Add CSS inline style to the component.

```dsl
impl object view list = Company.all >> grid {
    code
    name >> field(css = "background: red; color: white")
}
```

### Style declaration and modifier

Reference to style if you want to use a common style form few components.

```dsl
entity Company {
    field code: String
    field name: String
    object view list = Company.all >> grid {
        code >> field(style = fieldStyle)
        name >> field(style = fieldStyle)
    }
    style fieldStyle {
        "background: red;
        color: white"
    }
}
```

Here the `fieldStyle` style is declared. It is available also outside the entity by `Companies.fieldStyle` and can be declared in any place.
For example there could be a `class Styles` which contains all styles. It is a good practice if you use the same styles in different entities.
You can use selectors using `&` literal to refer the style name.

```dsl
style fieldStyle {
    "& > .field {
        color: red;
    }"
}
```


## Universal Modifiers

Some modifiers can be used for all layouts.


### `label`
Sets a label for layout which will be displayed in the header. By default, entity name will be used. It will be automatically translated into user-friendly string. For lists, singular form of entity name will be translated into plural. It does not work properly for all cases. So if plural for is incorrect, provide the `label` modifier.

```dsl
object view list = Company.all >> nav {
    table(label = “Companies”) {code, name}
}
```


### `visible`

Dynamic visibility of layout components.

```dsl
grid(visible = status == Bar) {
    code
    name
}
```


### `css`

Add CSS inline style to the component.


### `style`

Reference to style if you want to use a common style form few components.


### `span`

Allows to expand the field on more than one column in parent layout. Default value is `1`.


### `editMode`

- `Inherit`: use the same mode as in parent view, default.
- `AlwaysEdit`: element will be always in the edit mode.
- `AlwaysRead`: element will be always read only.
- `Inverse`: inverse the parent's mode so that it will be editable in the read mode and read only in edit mode.
