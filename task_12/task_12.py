# Runtime: 52 ms, faster than 80.17% of Python3 online submissions for Integer to Roman.
# Memory Usage: 13.9 MB, less than 95.33% of Python3 online submissions for Integer to Roman

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_symbols = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
            50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        out = ""
        for key in roman_symbols:
            if num // key > 0:
                out += roman_symbols[key] * (num // key)
                num -= (num // key) * key
        return out


if __name__ == '__main__':
    sol = Solution()
    nu = 1993
    print(sol.intToRoman(nu))
