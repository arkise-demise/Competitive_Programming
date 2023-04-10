class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = [None]*n
        for i in range(1,n+1):
            if i % 15 ==0:
                result[i-1] = "FizzBuzz"
            elif i % 5 ==0:
                result[i-1] = "Buzz"
            elif i % 3 ==0:
                result[i-1] = "Fizz"
            else:
                result[i-1] = str(i)
        return result                    