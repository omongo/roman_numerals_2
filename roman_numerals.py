class RomanNumerals:

    MAP = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def __init__(self, roman):
        self.roman = roman

    def get_int(self):
        if not self._valid():
            raise ValueError('It is not a Roman number.')
        MAP = RomanNumerals.MAP
        result, prev = 0, ''
        for char in self.roman:
            prev_lt_curr = (prev in MAP) and (MAP[prev] < MAP[char])
            result += MAP[char]
            if prev_lt_curr:
                result -= 2 * MAP[prev] 
            prev = char
        return result

    def _valid(self):
        MAP = RomanNumerals.MAP
        prev = ''
        count, prev_count = 0, 0
        for char in self.roman:
            count, prev_count = (count + 1, prev_count) if char == prev else (1, count)
            invalid_syntaxes = (
                char in ('I', 'X', 'C', 'M') and count > 3,
                prev in ('V', 'L', 'D') and (count > 1 or MAP[prev] < MAP[char]),
                prev in ('I', 'X', 'C') and (MAP[prev] * 10 < MAP[char] or prev_count > 1)
            )
            if any(invalid_syntaxes):
                return False
            prev = char
        return True

