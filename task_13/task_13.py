
class Solution:
    def roman_to_int(self, s: str) -> int:
        letters_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        exc_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        number_out = 0
        str_len = len(s)
        if str_len < 2:
            return letters_dict[s]
        i = 1
        while i < str_len:
            check_letters = s[i-1] + s[i]
            if check_letters in exc_dict:
                number_out += exc_dict[check_letters]
                i += 2
            else:
                number_out += letters_dict[s[i-1]]
                i += 1
        else:
            if s[-2] + s[-1] not in exc_dict:
                number_out += letters_dict[s[-1]]
        return number_out


if __name__ == '__main__':
    test_str = "MCMXCIV"
    out = Solution()
    print(out.roman_to_int(test_str))
