from typing import List

class Solution:
    def minCostToMoveChips(self,position: List[int]) -> int:
        even, odd = 0,0

        for x in position:
            if x%2==0:
                even+=1
            else:
                odd+=1

        return min(even, odd )

if __name__ == "__main__":
    positions = [1,2,3,6,4,7,6]
    sol = Solution()
    print(sol.minCostToMoveChips(positions))