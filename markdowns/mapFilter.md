We now come back to higher order functions. I will present `map` and `filter`, which both take a function and an iterator as parameters and return a new iterator. 

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


