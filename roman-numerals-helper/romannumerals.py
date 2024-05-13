# https://www.codewars.com/kata/51b66044bce5799a7f000003

roman_numerals = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}


class RomanNumerals:
    @staticmethod
    def to_roman(value: int) -> str:
        if value in roman_numerals.values():
            return [key for key, val in roman_numerals.items() if val == value][0]

        total_rom = ""

        while True:
            for key, val in roman_numerals.items():
                if (value - val) >= 0:
                    value -= val
                    total_rom += key
                    break
            if value == 0:
                break

        key_list = list(roman_numerals.keys())

        for k, v in roman_numerals.items():

            if total_rom == (k * 4):
                return f"{k}{key_list[key_list.index(k)-1]}"

            if total_rom.count(k) >= 4:
                start = total_rom.find((total_rom.count(k) * k))
                next_index = key_list[key_list.index(total_rom[start]) - 1]

                if start < 0:
                    end = start + 4
                elif total_rom[start - 1] != next_index:
                    end = start + 4
                else:
                    start = start - 1
                    end = start + 5

                total_rom = total_rom.replace(total_rom[start:end], f"{k}{key_list[key_list.index(total_rom[start]) - 1]}")

        return total_rom

    @staticmethod
    def from_roman(input: str) -> int:
        totalNum = 0

        if len(input) == 1:
            return roman_numerals[input]

        for key, value in enumerate(input):
            if key == 0:
                next = input[key+1]

                if roman_numerals[value] < roman_numerals[next]:
                    continue

                totalNum += roman_numerals[value]
                continue

            previous = input[key-1]
            if roman_numerals[value] > roman_numerals[previous]:
                totalNum += (roman_numerals[value] - roman_numerals[previous])
                continue
            if roman_numerals[value] == roman_numerals[previous]:
                totalNum += roman_numerals[value]
                continue
            if roman_numerals[value] <= roman_numerals[previous] and key == len(input) - 1:
                totalNum += roman_numerals[value]
                continue
            if roman_numerals[value] < roman_numerals[previous] and roman_numerals[value] >= roman_numerals[input[key+1]]:
                totalNum += roman_numerals[value]

        return totalNum


rm = RomanNumerals()
print(rm.from_roman("MCMXLIV"))  # 1944
print(rm.from_roman("XXI"))  # 21
print(rm.from_roman("MMVIII"))  # 2008
