# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution:         #this is the class named Solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:    #our method that we will be calling, this method will go ahead and take a list of integers numbers and another integer the target and itll return a list of two integers
        numsList = {}                       #the list of integers that we will be searching for our two numbers 
        for i,n in enumerate(nums):         #with this loop we will get both the index and the value (n) and the enumerate function will give us both values
            diff = target-n                 #diff means the difference between the target and the current number (n) it'll look for a sum to get us to the target 
            if diff in numsList:                #Checking to see if the calculated difference is already in the numsList
                return [numsList[diff], i]         #after checking if it is true it will return the two numbers that add up to the target
            else:                                   #if its not true then it will add the current number n and the loop will keep going until the solution is found
                numsList[n] = i


result = Solution()                  #here we are going to call the solution class which will be a result
finishedresult = result.twoSum([2], 12) #finished result is going to call our solution class which will be result = solution and then . the method and a integer and a target integer we want to aim for
print(finishedresult)       #print our finished result!











# If the loop completes without finding a solution, it implies that there are no two numbers in the list that add up to the target. In such a case, the function implicitly returns None.

# Overall, this algorithm efficiently finds a pair of indices representing two numbers in the list that sum up to the target, making use of a dictionary for fast lookup of previously encountered numbers.