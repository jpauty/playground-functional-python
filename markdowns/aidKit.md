Hi there, I'm Dr. Fun. Please describe your symptoms and I'll try to find the cure!

# I cannot find any place to use those fancy new functions I just discovered

Don't worry, this is quite normal. Functional programming addresses programming problems in a somewhat different way than imperative programming. Adopting a functional programming mindset takes time. The first step is to know that is exists and that it can bring useful solutions. With some practice, you will spot more and more places where you can use these functions.

Python does not enforce a programming style. You can progressively introduce functional constructions in your code. `any` and `all` are two functions that really improve code readability and which are easy to grasp. At first, you can try to keep them in your head and try to use them when needed. `sum`, `min` and `max` are also easy to use. After a while, you will be able to combine them.

If you want to take a more active approach to learning functional programming, you can select an algorithm you wrote recently and try to make it more functional. You can start with the method we applied to convert [factorial]((/markdowns/higherOrder.md):
 - identify the collection used by the algorithm;
 - identify the programming pattern;
 - look for matching functions.

If you need more help, we can go on with the consultation. Tell me more about your problem.   

# My code takes a collection and generates another collection

Right, I see. Our case probably belongs to the [first programming pattern](/markdowns/higherOrder.md).

## I want to remove unneeded items from the collection

Have look to `filter`. You may also use a generator expression with an `if` clause.  

## I want to convert the items of the collection

You'll probably feel better with a dose of `map`. If you prefer, you may also use a generator expression with an `if` clause.

## Someone made a mess in my collection

Don't worry, this is classic with collections. They often happen to be messy. I'll suggest a good old `sorted`.

## I would like to iterate several collections at the same time

Right, `zip` is a good candidate.

## I would like to combine several collections and create a new one

`zip` comes again to the rescue. You'll probably want to combine it with a generator expression. See our [dot product example](/markdowns/collections.md#dotProduct)

# My code takes an iterator and generates a single value

Just a moment. Yes, we'll probably heal you with the [second programming pattern](/markdowns/higherOrder.md#secondPattern).

## I would like assess a property on the collection

Have a look to `any` and `all`. You'll probably want to transform your collection with a generator expression before calling one these two functional workhorses.  

## I would like to compute a result out of the collection's items

If you're lucky, `sum`, `min`, `max` will do the job. Otherwise, have look to the next answer.

## I want to combine the collection's items with some random computation

I have something for you, but you may not like it: `reduce`. It's our all-in-one medicine, in a way or another it should cure you !

# I can't help creating classes and methods

This is good. The goal is not to stop using OOP. Like promoted by the [Scala programming language](http://scala-lang.org/), I would advocate to use OOP to architect your project with modules and classes, and to use functional programming for algorithms and manipulating data.

# I want to learn more !

I'm afraid you're developing an addition here. Good, this is very good! No need to cure you. Here are some learning resources that should fulfill your desire:
 * Python's [functional how-to](https://docs.python.org/3/howto/functional.html). It covers what we saw here, and much more functions. Especially the [functools module](https://docs.python.org/3/library/functools.html) which contains other useful functions such as `repeat` or `product`.
 * Learning a functional language such as [Ocaml](http://ocaml.org) or [Clojure](https://clojure.org/) is a good idea. Both are modern languages that are actively developed. There is also [Haskell](https://www.haskell.org/), but the road will be harder.  
 * If you really want to dive into functional programming, the reference book "Structure and Interpretation of Computer Programs" by Abelson, Sussman, and Sussman is a full textbook on functional programming. It's based on lisp, but the concepts and algorithms are applicable anywhere. It's progressive, so you will not drown into braces. Even better, the book is freely [available online](https://github.com/sarabander/sicp).

 