class Roman:
    def __init__(self):
        self.value_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]

    def int_to_roman(self, num: int) -> str:
        roman_numeral = ""
        for value, symbol in self.value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral


if __name__ == "__main__":
    convert = Roman()
    number = int(input("Enter an integer: "))
    result = convert.int_to_roman(number)
    print(f"The Roman numeral for {number} is: {result}")