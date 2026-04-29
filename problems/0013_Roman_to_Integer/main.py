class Solution:
    def romanToInt(self, s: str) -> int:
        digits = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        result = 0
        previous_value = 0
        for s in s[::-1]:
            current_value = digits[s]
            if current_value >= previous_value:
                result += current_value
            else:
                result -= current_value
            previous_value = current_value

        return result
