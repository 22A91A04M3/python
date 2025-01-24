############n=int(input())
##########lst=[]
########for i in range(n):
########    val=int(input())
########    lst.append(val)
########print(lst)
######----------------------
######nums =[10, 20, 30, 40, 50]
######new_list = []
######for i in nums:
######    new_list.append(i*i)
######print(new_list)
####---------------------
####n = int(input())
####lst = []
####for i in range(n):
####    name = input()
####    lst.append(ord(name[-1]))
####print(lst)
####------------------------   
##ages = [55, 92, 51, 31, 20, 75, 9, 35, 56, 62, 39, 58, 51, 63, 27, 12, 54, 56, 100, 79]
##children = []
##adult = []
##old = []
##for i in ages:
##    if i<=18:
##        children.append(i)
##    elif i>18 and i<=50:
##        adult.append(i)
##    else:
##        old.append(i)
##print(children, adult, old, sep='\n')
##--------------------------------
n=int(input())
lst1 = []
for i in range(n):
    name = input()
    lst1.extend(name)
print(lst1)   
