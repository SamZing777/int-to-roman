# Python3 program to convert
# integer value to roman values

# Function to convert Integer to Roman values
def printRoman(number):
	numbers = [1, 4, 5, 9, 10, 40, 50, 90,
		100, 400, 500, 900, 1000]
	symbols = ["I", "IV", "V", "IX", "X", "XL",
		"L", "XC", "C", "CD", "D", "CM", "M"]
	i = 12
	
	while number:
		circle = number // numbers[i]
		number %= numbers[i]

		while circle:
			print(symbols[i], end = "")
			circle -= 1
		i -= 1

# Function to convert Roman figure to Integer
roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
class Solution:
    def romanToInt(self, S: str) -> int:
        total = 0
        for i in range(len(S)-1,-1,-1):
            number = roman[S[i]]
            if 3 * number < total: 
                total = total - number
            else: 
                total = total + number
        print(total)

solution = Solution()
# print(solution = solution.romanToInt("D"))

# Input to convert Integer to roman
def convertIntToRoman():
        print("Convert Integer to Roman figure")
        print("NB: You can only enter number")
        num = int(input("Enter Integer: "))
        output = printRoman(num)
        return output


# Input to convert Roman Figure to integer
def convertRomanToInt():
        print("Convert Roman figure to Integer")
        print("NB: You can only enter roman figures")
        figure = input("Enter Figure: ")
        output = solution.romanToInt(figure)
        return output


# Function that calls the input
def takeInputAndConvert():
        print("Enter A to convert from Integer to Roman")
        print("Enter B to convert from Roman to Integer")

        value = input()

        if value == "A":
                return convertIntToRoman()
        elif value == "B":
                return convertRomanToInt()
        else:
                print("You can only enter values A or B")
        

takeInputAndConvert()




