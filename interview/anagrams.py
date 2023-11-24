# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

class Solution:         #our class
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:    #our method we will be calling, a list of strings as input and returning a list of lists of strings
        d = {}          #a empty list to store our anagrams
        for s in strs :     #loops through each string in the input list
            sorted_s = ''.join(sorted(list(s)))     #sorts the characters of s and then joins them back into a single string
            if sorted_s not in d :      #adds the orginial sring to the list of anagrams corresponding to the sorted string in the 'd' list
                d[sorted_s] = []            #if the sorted string is not already apart of the 'd' list a new list will be created for that key
            d[sorted_s].append(s)
        ans = list(d.values())              #creates a list of 'ans' containing values from the list 'd'
        return ans
    
result = Solution()                      #here we are going to call the solution class which will be a result

strs = ["cat", "dog", "tac", "god", "act", "mouse", "bird", "fish", "turtle"]       #list of anagrams we want to test and be grouped!

finishedresult = result.groupAnagrams(strs) #finished result is going to call our solution class which will be result = solution and then . the method and the strs of our anagrams

print(finishedresult)       #print our finished result!