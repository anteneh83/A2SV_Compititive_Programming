# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        rel=[]
        s=s.split()
        # print(s)
        max_len=max(len(w) for w in s)
        for i in range(max_len):
            temp=''
            for w in s:
                if i<len(w):
                    temp+=w[i]
                else:
                    temp+=' '
            rel.append(temp.rstrip())
        return rel
                



        