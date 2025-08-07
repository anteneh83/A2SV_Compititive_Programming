# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        x1=0
        x2=0
        if n%2 !=0:
            for num in nums2:
                x2^=num
        if m%2 !=0:
            for num in nums1:
                x1^=num
        return x1 ^ x2