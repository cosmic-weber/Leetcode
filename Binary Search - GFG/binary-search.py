#User function template for Python

class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
		return self.lst(arr, 0, n - 1, k)
		
	def lst(self, arr, i, j, k):
	    if j >= i:
	        m = (i + j) // 2
	        if arr[m] == k:
	            return m
	        elif arr[m] < k:
	            return self.lst(arr, m+1, j, k)
            else:
                return self.lst(arr, i, m - 1, k)
        else:
            return -1

#{ 
#  Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int, input().strip().split(' ')))
        k=int(input())
        ob = Solution()
        print (ob.binarysearch(arr, n, k))


# } Driver Code Ends