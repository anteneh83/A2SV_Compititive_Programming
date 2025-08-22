# Problem: Pow(x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        def pow(x, n):
            if x==0: return 0
            if n==0: return 1
            if n%2 !=0:
                res=pow(x, (n-1)//2)
                res=res*res*x
            else:
                res= pow(x, n//2)
                res=res*res``
            return res
        ans=pow(x, abs(n))
        if n>=0: return ans
        else: return 1/ans
                    