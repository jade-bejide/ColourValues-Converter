class ColourValues:
    def __init__(self, r, g, b):
        #records the decimal r, g and b values
        self.r = r
        self.g = g
        self.b = b
        #initialises the colour values (RGB and hex equivalent) as null
        self.hex_equivalent = None
        self.rgb_equivalent = None

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
        #switch case implementation to select letters corresponding to the numerical hex value
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
        #switch case implementation to select numbers corresponding to the alphabet hex value
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
        #stores the quotient 16 value
        first = value // 16
        #stores the modulus 16 value
        second = value % 16
        #if the two variables are more than 9, then the variables are converted to their alphabet equvalent
        if first > 9:
            first = self.convertToLetter(first)
        if second > 9:
            second = self.convertToLetter(second)

        first = str(first)
        second = str(second)

        return first + second

    def convertToRGB(self):
        #splits the hex_equivalent attributes to single digits
        first = self.hex_equivalent[1]
        second = self.hex_equivalent[2]
        third = self.hex_equivalent[3]
        fourth = self.hex_equivalent[4]
        fifth = self.hex_equivalent[5]
        sixth = self.hex_equivalent[6]

        #decimal values are found
        newR = int(self.convertToNumber(first)) * 16 + int(self.convertToNumber(second))
        newG = int(self.convertToNumber(third)) * 16 + int(self.convertToNumber(fourth))
        newB = int(self.convertToNumber(fifth)) * 16 + int(self.convertToNumber(sixth))
        #result is stored as a tuple
        RGBvalue = (newR, newG, newB)

        return RGBvalue

        

    def convertToHex(self):
        #converts r, g, b values from decimal to hex
        value1 = self.convertSectionsToHex(self.r)
        value2 = self.convertSectionsToHex(self.g)
        value3 = self.convertSectionsToHex(self.b)
        #sets hex_equivalent attribute to its corresponding hex value
        self.hex_equivalent = "#" + value1 + value2 + value3

        return self.hex_equivalent


