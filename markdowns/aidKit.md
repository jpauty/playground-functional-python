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

## I would like to combine several collections and create a new one

`zip` comes again to the rescue. You'll probably want to combine it with a generator expression. See our [dot product example](working-with-collections#dotProduct)

# My code takes an iterator and generates a single value

Just a moment. Yes, we'll probably heal you with the [first programming pattern](built-in-higher-order-functions-filter-map-and-reduce#secondPattern).

## I would like assess a property on the collection

Have a look to `any` and `all`. You'll probably want to transform your collection with a generator expression before calling one these two functional workhorses.  

## I would like to compute a result out of the collection's items

If you're lucky, `sum`, `min`, `max` will do the job. Otherwise, have look to the next answer.

## I want to combine the collection's items with some random computation

I have something for you, but you may not like it: `reduce`. It's our all-in-one medicine, in a way or another it should cure you !