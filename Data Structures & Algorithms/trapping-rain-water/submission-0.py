class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        water_trapped = 0
        left_maximum = 0
        right_maximum = 0

        while l < r:
        
            if height[l] <= height[r]:
                if height[l] >= left_maximum:
                    left_maximum = height[l]
                else:
                    water_trapped += left_maximum - height[l]
                
                l += 1
            else:
                if height[r] >= right_maximum:
                    right_maximum = height[r] 
                else:
                    water_trapped += right_maximum - height[r]
                r -= 1

        return water_trapped