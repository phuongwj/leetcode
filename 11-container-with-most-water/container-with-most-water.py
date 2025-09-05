class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)

        # initializing the left and right
        left = 0
        right = length - 1
        maxArea = 0

        for i in range(length):
            width = right - left

            if height[left] < height[right]:
                area = height[left] * width
            else:
                area = height[right] * width

            if area > maxArea:
                maxArea = area

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return maxArea

            