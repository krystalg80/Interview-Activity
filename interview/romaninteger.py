# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:             # our class
    def romanToInt(self, s: str) -> int:            #Our method, s will be our string for roman numeral and we are gonna convert it into the integer
        translations = {
            "I": 1,
            "V": 5,                         # the list of translations usually we would do a number list but since roman numbers are specific we will make a translations list
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")              #string.replace method is going to replace these phrases (roman numeral) into our translation which is the integer
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:                                          #char is a built in python function that represents our string which is the roman numeral and itll point to our integer 
            number += translations[char]                        #adds a value to an exisring variable so it will add the roman numeral together to get our translation             
        return number
    
result = Solution()         #here we are going to call the solution class which will be a result
finishedresult = result.romanToInt("VI")    #finished result is going to call our solution class which will be result = solution and then . the method and the roman numeral we want to translate
print (finishedresult)      #print our finished result!