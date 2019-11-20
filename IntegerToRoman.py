#https://leetcode.com/problems/integer-to-roman/

class intToRoman:

	def integerToRoman(self, decimalNumber):
		units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
		
		tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']

		hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

		thousands = ['', 'M', 'MM', 'MMM']

		return self.str(thousands[decimalNumber / 1000] +
				hundreds[(decimalNumber % 1000) / 100] +
				tens[(decimalNumber % 100) / 10] +
				units[decimalNumber % 10]



print(intToRoman().integerToRoman(400))
