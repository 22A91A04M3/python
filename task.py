n=int(input())
c=0
d=0
while n>0:
    c=n%10
    if(c%2==0):
        c=c+1
    else:
        d=d+1
        n=n//10
print(c,d)
    
