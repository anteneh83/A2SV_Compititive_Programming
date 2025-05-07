# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        def can_partition(sq_str, target, index, current_sum):
            if index == len(sq_str):
                return current_sum == target

            for i in range(index + 1, len(sq_str) + 1):
                part = int(sq_str[index:i])
                if can_partition(sq_str, target, i, current_sum + part):
                    return True

            return False

        total = 0

        for i in range(1, n + 1):
            square = i * i
            if can_partition(str(square), i, 0, 0):
                total += square

        return total
