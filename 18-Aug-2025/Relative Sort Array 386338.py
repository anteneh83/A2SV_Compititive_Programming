# Problem: Relative Sort Array - https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        # option 1

        map = defaultdict(int)
        for num in arr1:
            map[num]+=1
        # print(map)
        ans=[]
        map = dict(sorted(map.items()))
        for i in range(len(arr2)):
            while map[arr2[i]] !=0:
                ans.append(arr2[i])
                map[arr2[i]]-=1
        # print(ans)
        # print(map)
        for key, val in map.items():
            while val!=0:
                ans.append(key)
                val-=1

        # print(ans)
        return ans

        # option 2

        # temp = []
        # ans2=[]
        # for num in arr1:
        #     if num in arr2:
        #         temp.append(num)
        #     else:
        #         ans2.append(num)
        # # print(temp)
        # # print(ans2)
        # ans1=[]
        # map=defaultdict(int)
        # for num in arr1:
        #     map[num]+=1
        # # print(map)
        # for num in arr2:
        #     while map[num] !=0:
        #         ans1.append(num)
        #         map[num]-=1
        # # print(ans1)
        # return ans1 + sorted(ans2)

            