# Python Inheritance
Inheritance is the mechanism of deriving new classes from existing ones.Objects created through inheritance
acquires all of the property and behaviours of the parent object. This means that inheritance supports code
reusability. The class being extended is called the super class, base class or the parent class. The child class
is also known as the derived class.

**Benefits of inheritance are:**
- It represents real-world relationships well.
- It provides the reusability of a code. We don’t have to write the same code again and again. 
- Also, it allows us to add more features to a class without modifying it.
- It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of 
B would automatically inherit from class A.
- Inheritance offers a simple, understandable model structure. 
- Less development and maintenance expenses result from an inheritance
#### The syntax for inheritance is as follows
```
Class BaseClass:
	{Body}
Class DerivedClass(BaseClass):
	{Body}
```
*Python has two built-in functions that work with inheritance:*
* Use ```isinstance()``` to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int 
or some class derived from int.
* Use ```issubclass()``` to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. 
However, issubclass(float, int) is False since float is not a subclass of int.
## Multiple inheritance
Python supports a form of multiple inheritance as well. A class definition with multiple base classes looks like this:
```
class DerivedClassName(Base1, Base2, Base3):
	<statement-1>
	.
	.
	.
	.
	<statement- n>
```

**Different types of Inheritance:**
- Single inheritance: When a child class inherits from only one parent class, it is called single inheritance.
- Multiple inheritances: When a child class inherits from multiple parent classes, it is called multiple inheritances. 
- Multilevel inheritance: When we have a child and grandchild relationship
- Hierarchical inheritance More than one derived class are created from a single base.
- Hybrid inheritance: This form combines more than one form of inheritance. Basically, it is a blend of more than 
one type of inheritance.
