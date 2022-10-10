class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        
        for i in range(len(palindrome)):
            if palindrome[i] != 'a':
                srt = palindrome[:i]+'a'+palindrome[i+1:]
                if self.same(srt): 
                    break
                return srt
        
            
        n=len(palindrome)
        palindrome = palindrome[:n-1]+'b'
        # print(palindrome)
        return palindrome
    
    def same(self, srt):
        for i in range(1, len(srt)):
            if srt[0] != srt[i]:
                return False
        return True