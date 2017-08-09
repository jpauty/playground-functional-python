# Welcome!

This playground shows the useful, but lesser known, functional programming features of Python. Python is well known for its object oriented programming features: classes, methods, inheritance... However, Python is not restricted to object oriented programming, it offers several very useful features that enables the programmer to use the regular functional programming idioms, such as higher order functions and operations on data collections. These programming patterns are a useful addition to the arsenal of the regular Python developer.

I suppose here that: (1) you have basic knowledge of object oriented programming; (2) you have written a couple of Python programs. If you don't know Python, but know Javascript or Ruby, you should be able to follow this lesson easily.

# Higher order functions

One of the main concept of functional programming is *first class functions*. Simply said, it means that functions can be used like any other data type. You can :
 * store a function in a variable;
 * pass a function as an argument to another function;
 * return a function as the result of a function call;
 * make a list of function;
 * ...
 
A function that receives another function as an argument is called an higher order function. A well known higher order function of Python is `sorted`. In its simplest form, `sorted` can be used to sort a list of integers: `sorted([23,545,3])`. `sorted` has an optional argument `key`, which is a function with one argument. `sorted` will call the `key` function for each element and use the returned values to sort the list. Consider the following class, which models a bonus chest in an adventure game:

```python
class BonusChest(object):
	def __init__(self,x,y,numCoins):
		self.x = x
		self.y = y
		self.numCoins
	def getNumCoins(self):
		return self.numCoins
```

To sort a list of bonus chests with respect to the number of coins they contain, you can call: 
```python
sorted(chestList,key=BonusChest.getNumCoins)`.
``` 

`BonusChest.getNumCoins` is actually a function which takes a `BonusChest` instance as unique parameter.  `sorted` will call this function on each chest and use the result to sort them. Python calls such a function an unbounded method.

Getters and setters are less common within Python programs, so the instances you are sorting may not provide the needed `key` function to pass to `sorted`. You can create a function, outside the `BonusChest` class and pass it to `sorted`:

```python
def getNumCoins(chest):
	return chest.numCoins

sortedChests = sorted(chestList,key=getNumCoins)
```

Writing a separated function each time you want to sort a collection is not very practical, especially if this function will only be used by sorted. For such situations, Python offers the `lambda` keyword, which enables you to define a function on the fly: `sorted(chestList, key=lambda chest:chest.numCoins)`.   
Don't be afraid by the lambda keyword. Here, it just means: "I'm defining a function which takes a single argument `chest` and returns the value of the expression `chest.numCoins`. The body of lambda function is defined after the column and must be a single expression. The returned value is the value of this expression. Python uses the keyword `lambda` as a reference to Lambda calculus, the grand father of functional programming.


