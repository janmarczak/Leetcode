class Solution:
    def maxArea(self, height: List[int]) -> int:

        #     1   8   6   2   5   4   8   3   7
        # 1   X   1   2   3   4   5   6   7   8
        # 8   X   X   1   4   15  16  40  18  49
        # 6   X   X   X
        # 2   X   X   X   X
        # 5   X   X   X   X
        # 4   X   X   X   X
        # 8   X   X   X   X
        # 3
        # 7

        # for i in range(len(height) - 1):
        #     for j in range(i+1, len(height)):

        #         print(height[i], height[j])


        left = 0
        right = len(height) - 1 # 8
        maxArea = 0

        while left != right:
            area = min(height[left], height[right]) * (right - left)
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -=1

        return maxArea

        