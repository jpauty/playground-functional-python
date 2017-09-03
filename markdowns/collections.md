
Python comes with several useful built-in functions to work with collections. We saw `sorted` in the previous section, and you surely know `len` which returns the number of items in a collection. Here, I will present lesser known functions that can be truly useful: `any`, `all`, `zip`, `sum`, `min` and `max`.

# List comprehension and generator expressions

List comprehension enables you to transform a list into another list. For example, to create the list of the first 10 even numbers, we transform the list `[0,..,9]` : `evens = [n*2 for n in range(10)]`. Starting from Python 3, `range` does not return a list but a generator. So, to be precise, here we transform a range into a list. 

By adding an `if` clause, list comprehension can also be used to filter the source list. Here is another way to create the list of the first 10 even numbers: `evens = [n for n in range(20) if n%2 == 0]`.   

There are situations where the created list is only iterated once, typically in a for loop or as an argument of a function which expects an iterator. In these cases, you can use a generator expression instead of a list comprehension. A generator does not create the full list, but creates an iterator objects. The iterator expression is lazy, it will create the items on demand. When used in a for loop, a new item is generated at each iteration. A generator expression can possibly save a lot of memory and is more efficient. 

To create a generator expression, simply replace the surrounding brackets by braces: `evens = (n*2 for n in range(10))`. A generator expression can only be iterated once and cannot be accessed by index. Nevertheless, there are many cases where they can be used instead of a list comprehension.

# Tests on collections with `any` and `all`

We start with two very useful functions: `any` and `all`. They deserve a greater fame, because they enable compact and readable code.   

`any` and `all` take a single argument which must be a iterator, so they can handle lists, generator expressions, sets, dictionaries... `any` returns `True` if at least one element of the collection is true. Obviously, `all` returns `True` if all the elements of the collections are true. E.g. : 

```python
any([True,False,False]) # True
any([False,False,False]) # False
all([True,True,True]) # True
all([True,True,False]) # False
```

You might think that lists of booleans are not so common and that adding two built-in functions just for them is not very useful. However, with list comprehension you can easily transform an existing list into a list of booleans.

Consider a list of characters : `characterList`. With `all` you can write : 

```python
# Transform a list of character into a list of boolean.
# Each boolean represents the status of the character
if all([character.isDead for character in characterList]):
    lostGame()
```

instead of : 

```python
lost = True
for character in characterList:
    if not character.isDead:
        lost = False
        break

if lost:
    lostGame()
```

The call to `all` uses a generator expression. When you pass a generator expression to a single argument function, you can omit the surrounding braces.  

`any` and `all` are efficient, because they will stop the evaluation as soon as possible. `any` stops on the first true item. Conversely, `all` stops on the first false item. 

In the following exercise, you have to convert the code of `hasEven` by removing the loop and by using `any` or `all`. You will probably also need to use a generator expression.

@[Remove the loop and replace it by a call to any or all]({"stubs": ["anyAll.py"], "command": "python3 testAnyAll.py"})

# Combined iterations with `zip`

We now come to `zip`. With `zip` you can iterate several iterators at the same time. `list(zip([1,2,3],['a','b','c'])) == [(1,'a'),(2,'b'),(3,'c')]`. `zip` returns an iterator, so I made a `list` call in the previous expression for the sake of accuracy. `zip` works with iterators of different length. It stops at the end of the shortest iterator, so the length of the returned iterator is the length of the shortest parameter.  

The name zip is a bit confusing ; it has nothing to do with data compression. It refers to the ubiquitous fastener. A zipper takes two rows of teeth and binds the corresponding teeth. In a somewhat similar way, the `zip` function takes two lists and bind their items into pairs.   

At first glance, the use cases for `zip` seem less easy to find than for `any` or `all`. Nevertheless, `zip` comes in handy in many situations. Let's look at some examples. `zip` can be used to combine time series. Consider that you have two temperature sensors in a room, each one taking a measure every minute. At the end of the day, you have two lists of temperatures and you would like to build the list of mean temperatures.  

```python
dayMeanTemperatures = [] # will contain the mean temperature for today
# dayTemperatures is a method of Sensor which returns the list of temperatures for the current day
for temp1 temp2 in zip(sensor1.dayTemperatures(), sensor2.dayTemperatures()):
	dayMeanTemperatures.append((temp1 + temp2) / 2)
```
`zip` can be used with an arbitrary number of iterators, so this example can be generalized to more than two sensors.

Let's come back to a game oriented scenario. Consider the list `path=['A','B','C','D']` representing an ordered sequence, for example a path returned by a path finding algorithm. We would like to build the list of the edges which compose this path: `[(A,B),(B,C),(C,D)]`. This suspiciously looks like the result of a `zip` call, but can we use `zip` to build it ? If we take the first items of the pairs we get `[A,B,C]` and the second items give use `[B,C,D]`. So, we can write `zip(path[:-1],path[1:])`. Since `zip` stops at the end of the shorter iterator, we finally have:  

```python
path=['A','B','C','D']
edges = zip(path,path[1:])
```

A last example for the mathematically oriented readers. With `zip`, you can calculate the [dot product](https://en.wikipedia.org/wiki/Dot_product) of two vectors: 
```python
# vector1 and vector2 are two lists representing two vectors
dotProduct = 0
for v1Value, v2Value in zip(vector1,vector2):
    dotProduct += v1Value * v2Value
```

Often, when you iterate a collection you need the index of the current item. With `zip` you can write: 
```python
for index,character in zip(characterList,range(len(characterList)):
    doSomethingWithIndexAndCharater()
```

instead of the more error prone:

```python
index = 0
for character in characterList:
    doSomethingWithIndexAndCharater()
    index += 1
```

Actually, this pattern is so common that Python comes with a built-in function just for that: `enumerate`.
```python
for index,character in enumerate(characterList):
    doSomethingWithIndexAndCharater()
```
 
As I said before, `zip` is not limited to 2 iterators and works with an arbitrary number of iterators. Also, `zip` does not build a new collection, it returns an iterator that you can use in a `for` loop. If you want to reuse the result several times, you can build a list: `list(zip(coll1,coll2,coll3))`.  

In the following exercise you have to implement the `pairs` and `evenOdd` functions, which take a single `length` argument and return a list of pairs. For the `pairs` function, the n<sup>th</sup> returned pair is `(n,n+1)`, so `pairs(3)` returns `[(0,1),(1,2),(2,3)]`. For the `evenOdd` function, the n<sup>th</sup> returned pair is `(n*2,(n*2)+1)`, so `evenOdd(3)` returns `[(0,1),(2,3),(4,5)]`. To implement these two functions, you have use only the `zip` and `range` function.

@[Implement the pairs and evenOdd functions]({"stubs": ["rangeZip.py"], "command": "python3 testRangeZip.py"})

# Reducing functions: `sum`, `min` and `max`

In functional programming terminology, reducing a collection means iterating the collection in order to create a single value. `sum`, `min` and `max` all work on number collections, but with generator expressions their scope is much wider. For example:

```python
myScore = sum(chest.value for chest in chestList)
opponentStrength = max(character.strength for character in opponentList)
```

`min` and `max` do not support empty collections and will raise a ValueError exception when they receive one. `sum` returns 0  for an empty collection.
