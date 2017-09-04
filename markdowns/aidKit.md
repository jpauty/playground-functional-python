Hi there, please describe your symptoms and we'll try to find the cure !

# My code takes an iterator and generates another iterator

Right, I see. Our case probably belongs to the [first programming pattern](built-in-higher-order-functions-filter-map-and-reduce#firstPattern).

## I want to remove unneeded items from the collection

Have look to `filter`. You may also use a generator expression with an `if` clause.  

## I want to convert the items of the collection

You'll probably feel better with a dose of `map`. If you prefer, you may also use a generator expression with an `if` clause.

## Someone made a mess in my collection

Don't worry, this is classic with collections. They often happen to be messy. I'll suggest a good old `sorted`.

## I would like to iterate several collections at the same time

Right, `zip` is a good candidate.