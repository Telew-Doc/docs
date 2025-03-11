# Bugs

## `column` doesn't work in `view ref`

For original [references documentation](Data-Structure/Reference.md) an example of `#!dsl impl view ref = column { ... }` was used, but it produces some front-end errors.  
It's never used in the DSL apps, instead `y` can be seen which does work correctly.


## `row` layout renders in column when used in `ref` view

Again usage of `x` is preferrable, it behaves as expected.