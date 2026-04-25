# 12. Integer to Roman

class Solution:
    '''
    Step
        From smallest digit to greater digit
    Status: Failed
    Problem: Relatively complicated
    '''
    symbolMap = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    res = ""

    def intToRoman(self, num: int) -> str:
        digits = 1
        while num > 0:
            rem = num % (digits * 10)
            if rem == 4 * digits or rem == 9 * digits:
                res += symbolMap(digits) + symbolMap(rem + digits)
            else:

            num -= rem
        # not 4, 9:
        # consider decimal space
        # Subtract maximal value
        # 3 = 3 - 1 - 1 - 1
        # 30 = 30 - 10 - 10 - 10
        # 70 = 70 - 50 - 10 - 10
        # starts 4, 9: subtracted form IV IX XL XC CD CM
        # consider decimal space
        # 4 = 5 - 1, 9 = 10 - 1
        # 40 = 50 - 10, 90 = 100 - 10
        # power of 10: consecutive

class Solution:
    '''
    Step
        - From greater digit to smaller digit
        - Add extra information (900, 400, 90, 40...) to dictionary
    Status: Success
    '''
    def intToRoman(self, num: int) -> str:
        symbolMap = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        res = ""
        for val, sym in reversed(symbolMap.items()):
            div = num // val
            res += sym * div
            rem = num % val
            num = rem
        return res
