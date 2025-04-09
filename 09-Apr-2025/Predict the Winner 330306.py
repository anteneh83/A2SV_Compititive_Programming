# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        def play(rem, turn, score1, score2):
            if not rem:
                return score1 >= score2
            
            # choose 1, take left element
            c1 = play(
                rem[1:],
                2 if turn==1 else 1,
                score1 + rem[0] if turn ==1 else score1,
                score2 + rem[0] if turn ==2 else score2
            )

            # choose2, take right element
            c2= play(
                rem[:-1],
                2 if turn ==1 else 1,
                score1 + rem[-1] if turn ==1 else score1,
                score2 + rem[-1] if turn ==2 else score2
            )

            if turn == 1:
                return c1 or c2
            return c1 and c2

        return play(nums, 1, 0, 0)