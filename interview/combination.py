# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

class Solution:     #our class
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:    #our method takes integers as candidates and a integer target and it'll return a list of integers
        ans = []        #an empty list to store the final result of our combinations

        def bt(i, path, sum):       #i is the index in the candidates list, path is the current combination being considered, and the sum will be the sum of elements in the path
            if sum >= target:           #if current sum is greater than the target
                if sum == target: ans.append(path[:])   #if its exactly equal, the current combination path is added to the result

                return

            for j in range(i, len(candidates)):     #candidate is added to the current combination 'path'
                path.append(candidates[j])      #function is then called recursively with the updated index, combination, and sum
                bt(j, path, sum + candidates[j])    
                path.pop()

        bt(0, [], 0)        #the combinationSum is called with the starting index i = o and empty path and initial sum of 0

        return ans
    
result = Solution()                  #here we are going to call the solution class which will be a result
candidates = [2, 3, 6, 7]           #list of candidates
target = 7          #a target we set
finishedresult = result.combinationSum(candidates, target)         #finished result is going to call our solution class which will be result = solution and then . the method 
print(finishedresult)       #print finished result!
