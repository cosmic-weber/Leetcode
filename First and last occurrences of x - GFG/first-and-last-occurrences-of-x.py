#User function Template for python3


def find(arr,n,x):
    # code here
    return [leftSide(arr, x), rightSide(arr, x)]
    
def leftSide(arr,x):
    n = len(arr)
    i = -1
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            i = mid
            r = mid - 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return i
def rightSide(arr,x):
    n = len(arr)
    i = -1
    l, r = 0, n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            i = mid
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l = mid + 1
    return i

#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends