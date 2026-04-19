# 12. Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        # include special cases such as IX, CM... into hashmap in correct order
        hashmap = {
            'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V':5, 'IV': 4, 'I': 1
        }
        # itertively decrease the number toward zero using mod
            # divide num from largest to smallest using hashmap
        res = ""
        for k, v in hashmap.items():
            count = num // v
            if count > 0:
                res += count * k
            num %= v
        return res