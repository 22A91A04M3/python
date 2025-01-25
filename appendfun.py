Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=[10, 20, 30]
x.append(50)
print(x)
[10, 20, 30, 50]
x=[10, 20, 30]
x.append(50,70)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.append(50,70)
TypeError: list.append() takes exactly one argument (2 given)
x=[10, 20]
y=['a', 'b']
x.append(y)
print(x)
[10, 20, ['a', 'b']]
print(len(x))
3
x=[10, 20, 30]
y=['a', 'b', 'c']
x.append(y)
y.append(x)
x.append(y)
print(len(x))
5
#extend takes an iterable -> str, list, set, tuple
#Takes every value from the iterable and appends it to the list
#listname.extend(iterable)
x=[10, 20, 30]
x.extend(40)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x.extend(40)
TypeError: 'int' object is not iterable
marks = [35, 48]
marks.extend([56, 65, 76])
print(marks)
[35, 48, 56, 65, 76]
print(len(marks))
5
x = ['a', 'b']
y = "pqrstuvwxyz"
x.extend(y)
print(x)
['a', 'b', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(len(x))
13
alpha = []
alpha.extend("abcdefghijklmnopqrstuvwxyz")
print(alpha)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha = list(map(chr, range(97, 123)))
print(alpha)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = []
numbers.extend(range(1, 101))
print(numbers)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
n = []
n.extend(range(1, 11), end='\n')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    n.extend(range(1, 11), end='\n')
TypeError: list.extend() takes no keyword arguments
#insert()
#adds object at a specified index
#listname.insert(index,object)
x=[10, 20, 30]
x.insert(0, 40)
print(x)
[40, 10, 20, 30]
x.insert(0, 40)
x.insert(0, 'abcde')
x.insert(3, [70, 80, 90])
print(x)
['abcde', 40, 40, [70, 80, 90], 10, 20, 30]
x=[10,20,30]
x.insert(10, 50)
print(x)
[10, 20, 30, 50]
n=int(input())
lst=[]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    n=int(input())
ValueError: invalid literal for int() with base 10: 'lst=[]'
for i in range(n)
SyntaxError: incomplete input

================================== RESTART: C:/Users/K Gaythri/Desktop/append.py =================================
5
10
20
30
60
70
[10, 20, 30, 60, 70]

================================== RESTART: C:/Users/K Gaythri/Desktop/append.py =================================
Traceback (most recent call last):
  File "C:/Users/K Gaythri/Desktop/append.py", line 10, in <module>
    for i in nums:
NameError: name 'nums' is not defined

================================== RESTART: C:/Users/K Gaythri/Desktop/append.py =================================
[100, 400, 900, 1600, 2500]
ord(o)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    ord(o)
NameError: name 'o' is not defined
>>> 
>>> ord(n)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    ord(n)
NameError: name 'n' is not defined
>>> 
================================== RESTART: C:/Users/K Gaythri/Desktop/append.py =================================
4
tokyo
def
ghi
jkl
[111, 102, 105, 108]
>>> 
================================== RESTART: C:/Users/K Gaythri/Desktop/append.py =================================
[9, 12]
[]
[55, 92, 51, 31, 20, 75, 35, 56, 62, 39, 58, 51, 63, 27, 54, 56, 100, 79]
>>> 
================================== RESTART: C:/Users/K Gaythri/Desktop/append.py =================================
[9, 12]
[31, 20, 35, 39, 27]
[55, 92, 51, 75, 56, 62, 58, 51, 63, 54, 56, 100, 79]
>>> 
================================== RESTART: C:/Users/K Gaythri/Desktop/append.py =================================
3
xyz
abc
wer
['x', 'y', 'z', 'a', 'b', 'c', 'w', 'e', 'r']
