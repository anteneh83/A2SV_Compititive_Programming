# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []

        def backtrack(current, last_char):
            if len(current) == n:
                result.append(current)
                return

            backtrack(current + '1', '1')

            if last_char != '0':
                backtrack(current + '0', '0')

        backtrack("", "")
        return result