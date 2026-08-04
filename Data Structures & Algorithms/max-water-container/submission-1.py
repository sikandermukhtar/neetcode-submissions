class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maximum = 0

        while l < r: 
            # difference = abs(heights[l] - heights[r])
            level = min(heights[l], heights[r])
            # print("Level: ", level)
            water = (r - l) * level
            # print("Water:", water)

            maximum = max(water, maximum)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return maximum
