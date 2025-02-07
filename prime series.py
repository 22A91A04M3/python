def prime(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False
for i in range(10, 20):
    if prime(i) == True:
        print(i, end=' ')
