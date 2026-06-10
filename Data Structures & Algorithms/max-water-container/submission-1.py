class Solution:
    def maxArea(self, heights: List[int]) -> int:
        

        maxA = -math.inf

        l, r = 0, len(heights) - 1


        while l < r:

            height = min(heights[l], heights[r])
            width = r - l
            area = height*width
            maxA= max(maxA, area)

            if heights[r] > heights[l]:
                l+=1
            else: 
                r-=1
        return maxA


