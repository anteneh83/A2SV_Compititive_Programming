# Problem:  Gray Code - https://leetcode.com/problems/gray-code/description/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        for i in range(2**n):
            left_num = i >> 1
            gray = i ^ left_num
            ans.append(gray)
        # print(ans)
        return ans
        
