class Solution:
    def isHappy(self, n: int) -> bool:
        return self.Algo(n, {})
    
    def Algo(self, n, dict_):
        
        if n == 1:
            return True
        if n in dict_:
            return False
            
        lst, s = [], str(n)
        dict_[n] = 1
        for c in s:
            lst.append(int(c))
        n = 0
        for i in lst:
            n += i ** 2
        return self.Algo(n, dict_)