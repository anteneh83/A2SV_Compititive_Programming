# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n=len(s)
        ans=[]
        def backtrack(sol ="", i=0):
            if len(sol) == len(s):
                ans.append(sol[:])
            else:
                if s[i].isalpha():
                    backtrack(sol+s[i].swapcase(), i+1)
                backtrack(sol+s[i], i+1)
        backtrack()
        # print(ans)
        return ans

        



