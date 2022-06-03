class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[-1] += 1
        if len(digits) == 1 and digits[-1] > 9:
            return [1,0]
        elif digits[-1] > 9:
            carry = 1
            digits[-1] = 0
            i = len(digits) - 2
            while i >= 0:
                if i == 0 and digits[0] == 9:
                    digits.append(0)
                    digits[0] = 1
                    break
                
                
                digits[i] = digits[i] + carry 
                if digits[i] > 9:
                    digits[i] = 0
                    carry = 1
                else:
                    carry = 0
                    break
                i-=1
            return digits       
        else:
            return digits