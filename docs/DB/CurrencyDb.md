# Currency DB

## Rate class

### Properties

| # | NAME     | CLASS  | MANDATORY | READONLY | NOT-NULL |
|---|----------|--------|-----------|----------|----------|
| 0 | date     | NUMBER | true      | false    | false    |
| 1 | rate     | DATE   | true      | false    | false    |
| 2 | currency | STR    | true      | false    | false    |

> Records a rate by which certain currency goes under certain date.  
> Base currency is determined inside `currency` class

### Indexes

| # | NAME    | PROPERTIES       | TYPE   |
|---|---------|------------------|--------|
| 0 | rateIdx | [currency, date] | UNIQUE |

## Currency class

| # | NAME       | CLASS  | MANDATORY | READONLY | NOT-NULL |
|---|------------|--------|-----------|----------|----------|
| 0 | minDate    | DATE   | true      | false    | false    |
| 1 | invertBase | BOOL   | true      | false    | false    |
| 2 | minDelta   | NUMBER | true      | false    | false    |
| 3 | currency   | STRING | true      | false    | false    |
| 4 | maxDelta   | NUMBER | true      | false    | false    |
| 5 | base       | STRING | true      | false    | false    |
                          
> Specifying the `base` currency for each `currency` field.  
> 🚧 TODO: invertBase always true, what is it?  
> 🚧 TODO: minDate, minDelta and maxDelta meanings.

## Queries

- `select from rate`

| #  | @RID   | @CLASS | currency | date                | rate       |
|----|--------|--------|----------|---------------------|------------|
| 0  | #58:0  | rate   | BWP      | 2025-02-16 17:00:00 | 10.471     |
| 1  | #58:1  | rate   | SVC      | 2025-02-16 17:00:00 | 8.7495     |
| 2  | #58:2  | rate   | CLF      | 2025-02-16 17:00:00 | 0.024162   |
| 3  | #58:3  | rate   | NAD      | 2025-02-16 17:00:00 | 13.375     |
| 4  | #58:4  | rate   | JMD      | 2025-02-16 17:00:00 | 128.873255 |
| 5  | #58:5  | rate   | PAB      | 2025-02-16 17:00:00 | 0.999895   |
| 6  | #58:6  | rate   | WST      | 2025-02-16 17:00:00 | 2.50731    |
| 7  | #58:7  | rate   | XPD      | 2025-02-16 17:00:00 | 0.001488   |
| 8  | #58:8  | rate   | VUV      | 2025-02-16 17:00:00 | 107.379334 |
| 9  | #58:9  | rate   | AMD      | 2025-02-16 17:00:00 | 485.957501 |
| 10 | #58:10 | rate   | GBP      | 2025-02-16 17:00:00 | 0.798686   |
   
                    
- `select from currency`

| #  | @RID   | @CLASS   | currency | base | invertBase | minDelta | maxDelta | minDate             |
|----|--------|----------|----------|------|------------|----------|----------|---------------------|
| 0  | #57:0  | currency | TTD      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 1  | #57:1  | currency | BRL      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 2  | #57:2  | currency | MGA      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 3  | #57:3  | currency | SRD      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 4  | #57:4  | currency | SGD      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 5  | #57:5  | currency | GGP      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 6  | #57:6  | currency | HTG      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 7  | #57:7  | currency | GTQ      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 8  | #57:8  | currency | SOS      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 9  | #57:9  | currency | UYU      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |
| 10 | #57:10 | currency | TND      | USD  | true       | 3600     | 86400    | 1999-01-01 00:00:00 |