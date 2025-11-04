# Problem: Minimize XOR - https://leetcode.com/problems/minimize-xor/description/

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        ones = bin(num2).count('1')
        result = num1

        num1_count = bin(num1).count('1')

        if num1_count > ones:
            # turn off least bits
            for i in range(32):
                if num1_count == ones:
                    break
                if result & (1 << i):
                    result ^= (1 << i)
                    num1_count -=1

        else:
            # trun on least bit
            for i in range(32):
                if num1_count == ones:
                    break
                if not (result & (1 << i)):
                    result |= (1 << i)
                    num1_count +=1
        return result
        # print(result)
