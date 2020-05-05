class ColourValues:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.hex_equivalent = ""
        self.rgb_equivalent = (self.r, self.g, self.b)

    def get_r(self):
        return self.r

    def get_g(self):
        return self.g

    def get_b(self):
        return self.b

    def get_hex(self):
        return self.convertToHex()

    def get_RGB(self):
        return self.convertToRGB()

    def convertToLetter(self, value):
        if value == 10:
            return "A"
        elif value == 11:
            return "B"
        elif value == 12:
            return "C"
        elif value == 13:
            return "D"
        elif value == 14:
            return "E"
        elif value == 15:
            return "F"

    def convertToNumber(self, value):
        if value == "A":
            return 10
        elif value == "B":
            return 11
        elif value == "C":
            return 12
        elif value == "D":
            return 13
        elif value == "E":
            return 14
        elif value == "F":
            return 15
        else:
            return value



    def convertSectionsToHex(self, value):
        first = value // 16
        second = value % 16
        if first > 9:
            first = self.convertToLetter(first)
        if second > 9:
            second = self.convertToLetter(second)

        first = str(first)
        second = str(second)

        return first + second

    def convertSectionsToRGB(self, value):
        number = 0
        first = value[1]
        first = self.convertToNumber(first)
        second = self.convertToNumber(second)
        number = first * 16
        number += second
        

    def convertToRGB(self):
        first = self.hex_equivalent[1]
        second = self.hex_equivalent[2]
        third = self.hex_equivalent[3]
        fourth = self.hex_equivalent[4]
        fifth = self.hex_equivalent[5]
        sixth = self.hex_equivalent[6]

        newR = int(self.convertToNumber(first)) * 16 + int(self.convertToNumber(second))
        newG = int(self.convertToNumber(third)) * 16 + int(self.convertToNumber(fourth))
        newB = int(self.convertToNumber(fifth)) * 16 + int(self.convertToNumber(sixth))
        RGBvalue = (newR, newG, newB)

        return RGBvalue

        

    def convertToHex(self):
        value1 = self.convertSectionsToHex(self.r)
        value2 = self.convertSectionsToHex(self.g)
        value3 = self.convertSectionsToHex(self.b)
        self.hex_equivalent = "#" + value1 + value2 + value3

        return self.hex_equivalent

first = ColourValues(255, 0, 255)

print(first.get_hex())

print(first.get_RGB())
