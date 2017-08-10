
Python comes with several useful built-in functions to work with collections. We saw `sorted` in the previous section, and you surely know `len` which returns the number of items in a collection. Here, I will present lesser known functions that can be truly useful: `any`, `all` and `zip`.

# Tests on collections with `any`, `all` and list comprehension

`any` returns `True` if at least one element of the collection is true. Obviously, `all` returns `True` if all the elements of the collections are true. E.g. : 

```python
any([True,False,False]) # True
any([False,False,False]) # False
all([True,True,True]) # True
all([True,True,False]) # False
```

You might think that lists of booleans are not so common and that adding two built-in functions just for them is not very useful. However, with list comprehension you can easily transform an existing list into a list of booleans.

Consider a list of characters : `characterList`. With `all` you can write : 

```python
if all(character.isDead for character in characterList):
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

The call to `all` uses list comprehension to transform the list of characters into a list of boolean. You will remark that I did not surround the list comprehension with brackets. In this case, Python does not create a new list but an iterator. This avoids creating an intermediate list in memory, which would be used only once.

`any` and `all` are efficient, because they will stop the evaluation as soon as possible. `any` stops on the first true item. Conversely, `all` stops on the first false item. 

# Combined iterations with `zip`

With `zip` you can iterate several collections at the same time. For example :

```python
destinations = buildNextDestinations()
for character, destination in zip(characterList, destination):
    character.moveTo(destination)
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

Note that `zip` is not limited to 2 collections and works with an arbitrary number of collections. Also, `zip` does not build a new collection, it returns an iterator that you can use in a `for` loop. If you want to reuse the result several times, you can build a list: `list(zip(coll1,coll2,coll3))`.  

# Summing over a collection with `sum`
