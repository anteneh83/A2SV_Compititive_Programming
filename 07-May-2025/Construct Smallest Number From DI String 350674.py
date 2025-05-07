# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stk=[]
        ans=[]
        for i in range(len(pattern)+1):
            stk.append(i+1)

            if i==len(pattern) or pattern[i] == 'I':
                while stk:
                    ans.append(str(stk.pop()))

        return ''.join(ans)
