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
 * iterating a collection to build another collection. In this case, at each iteration, we want to apply some transformation or some test to the current item and append the result to the new collection. `map` and `filter` fall into this category.
 * iteration a collection and accumulating intermediate results to build a single value. For example, in an imperative manner, you would write: ```python
fact10=1
for n in range(1,10):
    fact10 = fact*n
``` `reduce` enable to perform the same computation, but written in a functional way.  

`map` and `filter` create an iterator from another iterator. 

