class Solution:
        def plusOne(self, digits: [int]) -> [int]:
            i = len(digits)-1
            isadd :int= 1
            while i >=0:
                if isadd == 0: break
                n = digits[i]
                if i == 0 and n==9:
                    digits[0] = 0
                    digits.insert(0,1)
                    break
                else:
                    n +=isadd
                    isadd = int(n/10)
                    n %=10
                    digits[i] = n
                i -= 1
            return digits
	