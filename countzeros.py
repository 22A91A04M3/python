#User function Template for python3
def countZeroes(arr):
        count=0
        for i in range(len(arr)):
            if(arr[i]==0):
                count+=1
        return count
arr = [1,0,0,0]
print(countZeroes(arr))

        # code here
