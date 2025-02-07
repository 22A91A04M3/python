Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/K Gaythri/Desktop/python/random.py
[10, 20]
x = [10, 20, 30, 40]
x.pop(3)
40
##remove()4
##remove is a element based deletion
##only the first occurance from left will be deleted
##list.remove(val)
##gives an error if vak is not present in the list
x=[10, 20, 30, 10]
x.remove(10)
print(x)
[20, 30, 10]

============= RESTART: C:/Users/K Gaythri/Desktop/python/random.py =============
[20, 30, 50, 25, 23]

============= RESTART: C:/Users/K Gaythri/Desktop/python/random.py =============
Traceback (most recent call last):
  File "C:/Users/K Gaythri/Desktop/python/random.py", line 25, in <module>
    while 'a' in names[i]:
TypeError: list indices must be integers or slices, not str
>>> 
>>> ord(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
>>> ord[a]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    ord[a]
NameError: name 'a' is not defined
>>> a=input()
ord(a)
>>> 
>>> ord('a')
97
>>> 
============================== RESTART: C:/Users/K Gaythri/Desktop/python/random.py ==============================
Traceback (most recent call last):
  File "C:/Users/K Gaythri/Desktop/python/random.py", line 25, in <module>
    while char(97) in names[i]:
NameError: name 'char' is not defined. Did you mean: 'chr'?
>>> 
============================== RESTART: C:/Users/K Gaythri/Desktop/python/random.py ==============================
Traceback (most recent call last):
  File "C:/Users/K Gaythri/Desktop/python/random.py", line 25, in <module>
    while chr(97) in names[i]:
TypeError: list indices must be integers or slices, not str
>>> 
============================== RESTART: C:/Users/K Gaythri/Desktop/python/random.py ==============================
['rocky']
