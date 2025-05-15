# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # xor = x ^ y
        # cnt = 0
        # while xor != 0:
        #     if xor & 1 == 1:
        #         cnt +=1
        #     xor = xor >> 1
        # # print(cnt)
        # return cnt
        return bin(x ^ y).count('1')