# Data Types

## Option T?

Optional data type allows empty value. For example:

```dsl
let company: Company?
```

can contain a company or null.

In this system, zero and empty strings are considered null and are empty values. This means that the `String` data type does not allow storing an empty string and `Int` does not allow storing zero. You need to use `String?` and `Int?`:

```dsl
let zero: Int = 0 // Wrong
let zero: Int? = 0 // Correct
let empty: String = "" // Wrong
let empty: String? = "" // Correct
```

Optional values are implicitly converted to `Bool`. It will be `true` if the value is not empty. It means that you can use it in conditions:

```dsl
let foo: String?
if (foo) {  // if (foo.isDefined)
} 
if (!foo) {  // if (foo.isEmpty)
}
```

### Functions

- `isEmpty: Bool`, `nonEmpty: Bool == isDefined: Bool`  
  Returns whether the option contains an item or nothing.

- `toSeq: [T]?`  
  Convert to collection. It will contain one element for a defined option or no element for an empty option.

- `in(collection: [T]?): Bool`  
  It checks whether the value contains in the collection. If the option is empty it returns false.

- `all(predicate: T => Bool): Bool`  
  It returns true if the predicate is true for the value or the option is empty.

- `exists(predicate: T => Bool): Bool`  
  It returns true if the predicate is true for the value. If the option is empty, it returns false.

- `filter(predicate: T => Bool): T?`  
  Returns the same option if the predicate is true or empty if it's false.

- `map[T1](f: T => T1): T1?`  
  Maps the value of the option with f or returns empty.

- `flatMap[T1](f: T => T1?): T1?`  
  Maps the value of the option with f or returns empty.

- `alt(default: () => T): T`  
  Returns the value or alternatively the default value if the option is empty.

- `or(default: () => T?): T?`  
  Return the same option if it's defined or the option returned by the default function.

## Dec, Money, Qty, Int, Percent, Num

Decimal data type.

- `Dec` does not allow storing zero.
- `Dec?` allows storing all values including zero.
- `UDec` does not allow negative values and zero.
- `UDec?` allows string zero and positive types

It can have two data type parameters: unit and precision:

```dsl
let foo: Dec[ProductUnit.Kilogram, 4] = 2.1  // 2.1000 gram
let foo: Dec[2] = 2.1  // 2.10
let foo: Dec[ProductUnit.Kilogram] = 2.1  // 2.100 gram
```

The unit should be of the `Unit` data type.

If you add a unit without a precision, it will use the default precision returned by the Unit.

The unit can be dynamic and stored in a structure. For example:

```dsl
field unit: ProductUnit
field foo: UDec[unit]?
```

### Data type inference

If you do math operation, the compiler infers the result data type and computes whether it's always positive and optional. Rules:

```dsl
(Dec|Dec?) + (Dec|Dec?|UDec|UDec?) = Dec?
UDec? + (UDec|UDec?) = UDec?
UDec + UDec = UDec
(Dec|Dec?|UDec|UDec?) - (Dec|Dec?|UDec|UDec?) = Dec?

Dec? * (Dec|Dec?|UDec|UDec?) = Dec?
UDec? * Dec = Dec?
UDec? * (UDec|UDec?) = UDec?
Dec * (Dec|UDec) = Dec
UDec * UDec = UDec

Dec? / (Dec|UDec) = Dec?
Dec / (Dec|UDec) = Dec
UDec? / Dec = Dec?
UDec? / UDec = UDec?
UDec / Dec = Dec
UDec / UDec = UDec

-Dec? = Dec?
-Dec = Dec
-UDec = Dec
-UDec? = Dec?
```

### Decimal Types

- `Dec`, `UDec`  
  It's a generic decimal type without additional context.

- `Money`, `UMoney`  
  Money is a decimal type which takes a currency as a unit.

    ```dsl
    let foo: UMoney[USD]? = 20 // $20.00
    ```

- `Qty`, `UQty`  
  It's a `Dec` alias and can take any unit as a parameter. Use it to explicitly make quantity.

- `Int`, `UInt`  
  `Int` does not have parameters. It's a decimal with 0 precision and no unit.

- `Percent`, `UPercent`  
  This data type has the `Percent` as a unit. It has precision as a parameter. By default, the precision is 2. It means that it can store 10% but not 10.1%.

    ```dsl
    let foo: Percent? = 0.1 // 10%
    let foo: UPercent[2] = 0.321 // 32.10%
    ```

- `Num`, `UNum`  
  It's a generic interface which can be any numeric type.

## Bool

Boolean datatype. Can be either `true` or `false`.

## String

String datatype.

- `dropPrefix(prefix: String): String`, `dropPrefixes(prefixes: [String]): String`  
  If the string starts with the prefix it drops it otherwise it returns unmodified string. The `dropPrefixes` function call `dropPrefix` in the cycle for every prefix.

    ```dsl
    "www.google.com".dropPrefix("www.") == "google.com"
    "google.com".dropPrefix("www.") == "google.com"
    "https://www.google.com".dropPrefixes(["http://", "https://", "www."]) == "google.com"
    ```

- `dropSuffix(suffix: String): String`, `dropSuffixes(suffixes: [String]): String`  
  If the string ends with the suffix it drops it otherwise it returns unmodified string. The `dropSuffixes` function call `dropSuffix` in the cycle for every suffix.

    ```dsl
    "www.google.com".dropSuffix(".com") == "www.google"
    ```

## Text

Formatted text. Multiline string editor will be used for fields with this type. The same functions can be applied for text as for string.

## Date, Duration

### Date

`Date` data type has two optional parameters which determine a lower and upper date units:

- `Date[day, year]` or simply `Date[day]` will store a date only without time
- `Date[millisecond, hour]` is the same as the `Time` data type
- `Date[month, year]` or `Date[month]` will store date only month and year
- `Date[millisecond, year]` is the same as simply `Date` will store the whole date

Available time units are: millisecond, second, minute, hour, day, week, month, quarter and year.

### Timezone and UTC

By default date will have timezone information if the lower unit is not higher than an hour and the upper unit is year. Otherwise, it will be always considered as UTC timezone.

You can force `Date` not to have timezone information by using `UtcDate` instead of `Date`.

If the code is executed on a client `Date` will have user's local timezone. If the code is executed on the server the timezone will be in the Workspace timezone. If you want to change a timezone, use the `timezone(zone: String): Date`.

### Duration

`Duration` data type is a number and has two parameters: time unit and precision. `Duration[day]` - duration in days, `Duration[day, 10]` - duration in day with 10 numbers after dot.

As other number you can form duration by number underscore and unit:

```dsl
let dur: Duration = 1_day
```

You can add duration to dates:

```dsl
Date(2017, 12, 8) + 1_day == Date(2017, 12, 9)
```

Difference between days will return duration:

```dsl
Date(2017, 12, 9) - Date(2017, 12, 8) == 1_day
```

You can make operations on durations in different units:

```dsl
1_hour + 1_day == 25_hour
```

## Map

Contains correlations between key (K) and value (V): `[Int: String]`, `[Company: Dec[2]]`.

- `agg[I, V1 where V = [I] => V1): [K : V1]`  
  Aggregate values if they are collection. Usually it is used along with the group function.