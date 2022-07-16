class Solution:
    def isHappy(self, n: int) -> bool:
        return self.Algo(n, [])
    
    def Algo(self, n, lst1):
        
        if n == 1:
            return True
        if n in lst1:
            return False
            
        lst, s = [], str(n)
        lst1.append(n)
        for c in s:
            lst.append(int(c))
        n = 0
        for i in lst:
            n += i ** 2
        return self.Algo(n, lst1)