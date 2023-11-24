# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.
class Solution:                                 #Our class which is where our method will go
    def intToRoman(self, num: int) -> str:      #our method and just like the last one of roman to integer, we will be converting our integer/number to our roman numeral which will be our string
        roman_numerals = {                      #instead of translations from roman numeral to integers, we will be using our integers to give us our roman numeral
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",                
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }

        result = ""         #will give us a empty string to store our data/numerals that we will call
        for value, symbol in roman_numerals.items():    #the loop will go through items in our roman_numerals list
            while num >= value:     #checks how many times the current value can be subtracted from the given number
                result += symbol        #each substraction it appends the symbol to the result string
                num -= value            #updates number by subtracting the value

        return result

# Example usage:
result = Solution()              #here we are going to call the solution class which will be a result
finishedresult = result.intToRoman(27)      #finished result is going to call our solution class which will be result = solution and then . the method and the integer we want to calculate into a roman numeral
print(finishedresult)                       # this should give us 27 which is Output: "XXVII"
