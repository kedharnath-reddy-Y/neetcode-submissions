class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maxThree = ""
        for i in range(len(num)-2):
            three_digit=num[i:i+3]
            if three_digit[0] == three_digit[1] == three_digit[2]:
                if three_digit > maxThree:
                    maxThree = three_digit
        return maxThree


        
        