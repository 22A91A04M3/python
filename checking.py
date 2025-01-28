Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = [1, 2, 3, 4, 5]
print(type(a))
<class 'list'>
a = 10.5
print(type(a))
<class 'float'>
a = [1, 2, 2]
print(a)
[1, 2, 2]
a=[10, 20, 30, 40, 50]
print(type(a))
<class 'list'>
a.append(60)
print(a)
[10, 20, 30, 40, 50, 60]
a.pop(1)
20
a.remove(5)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.remove(5)
ValueError: list.remove(x): x not in list
a.remove(60)
print(a)
[10, 30, 40, 50]
a=[1 , 2, (4, 2)]
print(a)
[1, 2, (4, 2)]
print(type(a))
<class 'list'>
a=(1 2 4)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a=(1, 2, 4)
print(type(a))
<class 'tuple'>
<class 'tuple'>
SyntaxError: invalid syntax
a=(1, 2, 3)
print(a)
(1, 2, 3)
a=[1, 2, 3, 4]
a(set(2))
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a(set(2))
TypeError: 'int' object is not iterable
>>> print(a(set(2))
...       a(2)
...       
SyntaxError: '(' was never closed
>>> a={1, 2, 3}
...       
>>> print(a)
...       
{1, 2, 3}
>>> print(type(a))
...       
<class 'set'>
>>> a={"Gayatri"}
...       
>>> print(a)
...       
{'Gayatri'}
>>> a={'1', 'sai', 2 3}
...       
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a={'1', 2, 'sai', 3}
...       
>>> print(a)
...       
{'sai', 2, 3, '1'}
>>> a={1, 2, 2}
...       
>>> print(a)
...       
{1, 2}
>>> a=10
...       
>>> print(type(a))
...       
<class 'int'>
