Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1, 2, 4, 6]
>>> a
[1, 2, 4, 6]
>>> a[2]
4
>>> x
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> len(a)
4
>>> a.append(20)
>>> a
[1, 2, 4, 6, 20]
>>> a.remove(4)
>>> a
[1, 2, 6, 20]
>>> k=[12, 'sai', 2.2, 1+5j]
>>> a.append('hari')
>>> a
[1, 2, 6, 20, 'hari']
>>> [1, 2, 6, 20, 'hari']
[1, 2, 6, 20, 'hari']
>>> a.remove(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    a.remove(3)
ValueError: list.remove(x): x not in list
>>> a.remove(6)
a
[1, 2, 20, 'hari']
