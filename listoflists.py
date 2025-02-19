######
########x = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
########print(x[1][1])
########print(x[0][2])
########print(x[2][1])
#######Matrices as User inuts
######r,c = map(int,input().split()) #reading rows and columns
######mat = []
######for i in range(r):
######    inner_list = list(map(int,input().split()))[:c:]
######    mat.append(inner_list)
######print(mat)
#####How to run a loop on Matrix(2-d lists)
#####Element based looping
####r = 3
####c = 3
####mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
####for inner_list in mat:
####    for every_value in inner_list:
####        print(every_value, end=' ')
####    print()
###Adding matrix elements together
##r,c = map(int,input().split())
##mat = []
##for i in range(r):
##    inner_list = list(map(int,input().split()))[:c:]
##    mat.append(inner_list)
##s=0
##for inner_list in mat:
##    for every_value in inner_list:
##        s += every_value
##print(s)
#Index based access on a Matrix
r = 3
c = 3
mat = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
for i in range(r):
    for j in range(c):
        print(mat[i][j], end = ' ')
    print()
