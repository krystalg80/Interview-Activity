# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

class Solution:                 #Class which is where our method will go in and etc 
    def maxArea(self, height: list[int]) -> int:            #this is the method and instead we will add the height in an inteer form and then eventually get the integer form 
         l,r=0,len(height)-1                      #the length is (l) and r means that the beggininug numerbve

         water = 0         #this is a variable to store the maximum area
         while l<r:           #this is the main loop and it will continue as long as l and less than r 
            water=max(min(height[l],height[r])*(r-l),water)      #this is very long but it calculates the two bars at 'l' and 'r' and it updates the water
            if height[l]<height[r]:     #if height at index is less than the height at r , then move l to the right
                 l+=1
            else:                       #if its more than then move r to the left
                 r-=1
 
         return water

result = Solution()                      #here we are going to call the solution class which will be a result
heights = [1,5,12,20]                             #the heights we are giving the containor to calculate   
finishedresult = result.maxArea(heights)               #finished result is going to call our solution class which will be result = solution and then . the method and the heights we want to calculate         
print(finishedresult)              #print our finished result!


