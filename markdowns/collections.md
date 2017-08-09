
Python comes with several useful built-in functions to work with collections. We saw `sorted` in the previous section, and you surely know `len` which returns the number of elements in a collection. Here, I will present lesser known functions that can be truly useful: `any`, `all` and `zip`.

# Tests on collections `any`, `all`

`any` returns `True` if at least one element of the collection is true. Obviously, `all` returns `True` if all the elements of the collections are true.

Consider you have a list of characters : `characterList`. With `all` you can write : 

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