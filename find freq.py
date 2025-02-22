def findFrequency(arr, x):
    count = 0
    for i in arr:
        if i==x:
            count += 1
    return count
x = int(input())
arr = list(map(int,input().split()))
print(findFrequency(arr, x))
