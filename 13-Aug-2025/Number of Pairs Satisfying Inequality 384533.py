# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        difference=[a-b for a, b in zip(nums1, nums2)]
        # print(difference)
        aux=[]
        res=0

        for d in difference:
            cnt = bisect.bisect_right(aux, d)
            res+=cnt
            bisect.insort(aux, d-diff)
        return res


