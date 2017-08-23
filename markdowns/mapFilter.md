We now come back to higher order functions. I will present `map`, `filter` and `reduce`. Like `sorted`, these functions take a function and an iterator as parameters. 

# Converting the items of a collection with `map`.

`map` creates a new collection by applying a function to each item of the source collection. To get the 10 first even numbers, with `map` you can write: `evens = map(lambda n: n*2, range(10))`.

`map` returns an iterator. The good point is that it saves memory. The bad point is that it can be iterated only once. If you need to iterate the collection several times, or access items by index, then create a list out of the iterator: `evens = list(map(lambda n: n*2, range(20)))`.

Most of the time, you can use a generator expression instead of a call to `map`. Which one to use is up to your preferences. If you have to define a function inline using `lambda`, then I think a generator expression will be a bit more clearer than a call to `map`. However, if the mapping function already exists then I prefer a call to `map`. Compare for yourself:

```python
# we reuse the class BonusChest of the introduction
wealthMap = sum(map(BonusChest.getNumCoins, myChests))
wealthGen = sum(chest.getNumCoins() for chest in myChests)
```

# Filtering collections with `filter`

 `filter` applies a function to each item of the source collection and create a new one by keeping the items for which this function returns true.

Again, to get the 10 first even numbers, with `map` you can write: `evens = filter(lambda n: n%2==0, range(20))`.

Like `map`, most of the time you can replace a call to `filter` by a generator expression: `evens = (n for n in range(20) if n%2 == 0)`.  

# Aggregating a collections to a single value with `reduce`

When we work with collections, two very common programming patterns emerge: 
 * *iterating a collection to build another collection.* In this case, at each iteration, we want to apply some transformation or some test to the current item and append the result to the new collection. `map` and `filter` fall into this category.
 * *iterating a collection and accumulating intermediate results to build a single value.* For example, to calculate factorial(10): (1) the accumulated value starts at 1; (2) you will iterate through the list `[1,...,10]`; (3) at each iteration the accumulated value is multiplied by the current item.   
 
 In an imperative manner, you would compute factorial(10) in the following way: 
```python
def factorial(n):
    fact = 1
	for n in range(1,10):
      fact = fact*n
    return fact
fact10 = factorial(10) 
```

In a functional manner, you would compute factorial(10) in the following way:
```python
from functools import reduce
from operator import mult

def factorial(n):
	return reduce(mult,range(1,n),1)
    
fact10 = factorial(10) 
```

Let's ignore the imports for a moment and study the `reduce` call.  `reduce` takes 3 arguments: 
 1. an accumulating function which takes 2 arguments : (1) the current accumulated value; (2) the current item. It return the final accumulated value.
 1. an iterator;
 1. an initial value for the accumulated value.
`reduce` returns the final accumulated value.

So, the call `reduce(mult,range(1,n),1)` says: "I want to accumulate over the values from 1 to n, starting with an accumulated value of 1 and by multiplying the current accumulated value with the current item." You might think that calls to reduce are abstract and hard to understand, but it is really a matter practice. A benefit of functional programming is that it simplifies the reading of programs. When reading from left to right, you read first the outer function, which gives the general scope of the operation. Arguments gives you the details. Let's how this applies to a our `reduce` call. When you see `reduce`, you know that we will process an iterator and generate a value. This our second functional pattern. Then, you read the accumulating operation, `mult` in our example. So, at this point, we know that we will perform a sequence of multiplication and return the final value. The next argument tells us what is the sequence of multiplied numbers. The final argument tells from where we start.

If you compare the two versions of factorial, you will see that `reduce:
 1. gives us a more compact code, without sacrifying readability;
 1. is less error prone, because it does not rely on an intermediate variable that you have to declare, initialize and maintain in the for loop. 

We can now come back to the two import calls. Starting from Python 3, you must import `reduce` from the `functools` module. In Python 2, reduce was a built-in function and was always available. Even if `reduce` is not a built-in function per-se anymore, we cannot skip it ; we would loose a whole part of the functional programming fun. `reduces` is really the buddy of `map` and `filter`. See for example the [MapReduce](https://en.wikipedia.org/wiki/MapReduce) of Google.

Next, we import the `mult` function from the `operator` module. This module contains many utility functions which are particularly useful with higher order functions. They spare you from writing small lambda functions for common operations, such as arithmetic operations, boolean operations, attribute access...   

`reduce` really shines if you can avoid defining a `lambda`. Without the `operator` module we would write:
```python
from functools import reduce

def factorial(n):
	return reduce(lambda accValue,curItem:accValue*curItem,range(1,n),1)
``` 
This version is arguably not very readable and should be avoided.

In that case, I would advise to skip the `lambda` function, and to define the `mult` function yourself:
```python
from functools import reduce

def factorial(n):
	def mult(a,b): return a*b
	return reduce(mult,range(1,n),1)
``` 
