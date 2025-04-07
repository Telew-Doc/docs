# Operators

## Assignment Operator

`=` - Set operator changes value of the left operand to the value of right operand:

```dsl
price = total/qty
```

## Dot Operator

`.` - Get item property:

```dsl
entity Product { 
    field supplier: Company 
    func supplierName: String = supplier.name 
}
```

## Optional Dot Operator

`?.` - If an item is optional and you want to get its property, you can use the optional dot operator. This will return an optional value as well:

```dsl
entity Product { 
    field supplier: Company? 
    func optionalSupplierName: String? = supplier?.name 
}
```

If the right operand is also optional, this operator will join two optional values and return optional instead of optional of optional. If the right operand is also collection, this operator will return a collection instead of an optional collection.

```dsl
class InvoiceItem { 
    field product: Product? 
    func productColor: Color? = product?.color 
    func productSuppliers: [Company] = product?.suppliers 
} 

entity Product { 
    field color: Color? 
    field suppliers: [Company] 
}
```

## Option Unwrap Operator

`!` - Unwrap option value. If option is empty, computation will fail:

```dsl
entity Product { 
    field supplier: Company? 
    func notOptionalSupplier: Company = supplier! 
    func notOptionalSupplierName: String = supplier!.name 
}
```

## Collection Dot Operator

`*.` - This operator takes a collection and returns another collection of field values:

```dsl
entity Product { 
    field suppliers: [Company] 
    func supplierNames: [String] = suppliers*.name 
}
```

If the right operand is also optional, this operator will return collection of only full fields instead of collection of options. If the right operand is also collection, this operator will join the collections and return one collection instead of collection of collections.

```dsl
class Invoice { 
    field products: [Product]
    func productColors: [Color] = product*.color 
    func productSuppliers: [Company] = product*.suppliers 
} 

entity Product {
    field color: Color? 
    field suppliers: [Company] 
}
```

## Substring Operators

`[ .. ]`, `( .. )`, `[ .. )`, `( .. ]` - These operators allow getting substring for a string. The index of the first element is 0.

```dsl
"Test"[1 .. 2] == "es"
```

It applies for a string and can have two arguments. These two arguments can be either an index or a substring to search:

```dsl
"Test string"["es" .. "r"] == "est str"
```

You can omit an expression from one of the sides, then it will start from the beginning or end of the string:

```dsl
"Test string"[ .. "r"] == "Test str"
```

You can use round brackets instead of square in one or on both sides. Then the position will be excluded from the range:

```dsl
"Test string"["es" .. "r"] == "est str" 
"Test string"("es" .. "r"] == "t str" 
"Test string"["es" .. "r") == "est st" 
"Test string"("es" .. "r") == "t st" 
"Test"[1 .. 2] == "es" 
"Test"(1 .. 2] == "s" 
"Test"[1 .. 2) == "e" 
"Test"(1 .. 2) == ""
```

You can get a substring from the last position in the string using `.last`:

```dsl
"First.second.third"(".".last .. ] == "Third"
```

You can make an optional substring when it will return the string from the start or till the end if the value is not found. You need to use `?` for this:

```dsl
"first/second"("/" .. ".") == "" 
"first/second"("/" .. "."?) == "second"
```

## Math Operators

### Addition (`+`)
Add two numeric values or concatenate strings:

```dsl
1 + 2 == 3
"1" + "2" == "12"
"1" + 2 == "12"
```

Additionally, you can join two collections together or add an element to the collection:

```dsl
[1, 2] + [2, 3] == [1, 2, 2, 3]
[1, 2] + 3 == [1, 2, 3]
1 + [2, 3] == [1, 2, 3]
```

### Subtraction (`-`)
```dsl
1 - 2 == -1
```

### Multiplication (`*`)
```dsl
2 * 3 == 6
```

### Division (`/`)
```dsl
6 / 2 == 3
```

### Power (`pow`)
Exponent. It returns with the same precision as the first argument:

```dsl
2.pow(3) == 8
2.00.pow(-1) == 0.5
2.as[Number[4]].pow(2.5) == 5.6569
```

## Comparison Operators

### Equal (`==`)
Equal operator returns true if two values are equal:

```dsl
1 == 1 == true
```

### Not Equal (`!=`)
Not equal operator returns true if two values are not equal:

```dsl
1 != 1 == false
```

### In (`in`)
Checks whether the value contains in a collection:

```dsl
3 in [1, 3, 6]
```

Optional values can be used:

```dsl
let role: Role? = Salesperson
role in [Salesperson, BusAdmin]
```

The right side can be any expression, not only a collection constant:

```dsl
let options = [1, 3, 6]
x in options
```

Not in will be:

```dsl
2 !in [1, 3, 6]
```

### Greater (`>`)
```dsl
2 > 1
```

### Greater or Equal (`>=`)
```dsl
2 >= 1
```

### Less (`<`)
```dsl
1 < 2
```

### Less or Equal (`<=`)
```dsl
1 <= 2
```

## Conditional Comparison Operators

`==?`, `?==`, `!=?`, `?!=`, `>?`, `?>`, `>=?`, `?>=`, `<?`, `?<`, `<=?`, `?<=`

The operators do the same as conditional operators but they will accept one optional side. If it's empty, it will return true. Otherwise, it will return the result of the conditional operation.

It's very convenient for conditional filtering in reports:

```dsl
foo >? lowerFoo
```

Instead of:

```dsl
!lowerFoo || foo > lowerFoo!
```

## Logical Operators

### Not (`!`)
The inverse unary logical operator returns true if the operand is false and vice versa:

```dsl
!true == false
!false == true
```

### And (`&&`)
Logical and operator returns true only if both operands are true otherwise false:

```dsl
true && true == true 
true && false == false
```

### Or (`||`)
Logical or operator returns false only if both operands are false otherwise true:

```dsl
false || false == false 
true || false == true
```

## Operator Order

Binary operators have a natural order and you can use brackets to control the order:

```dsl
1 + 2*3 == 1 + (2*3) != (1 + 2)*3
```

If operators are in the same group the order will be from left to right.

Order of operations (from highest to lowest precedence):
1. `=`
2. `||`
3. `&&`
4. `==`, `!=`, `>`, `>=`, `<`, `<=`
5. `+`, `-`
6. `*`, `/`