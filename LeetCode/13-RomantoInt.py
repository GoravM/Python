dict = {
    "I" : 1,
    "IV" : 4,
    "V" : 5,
    "IX" : 9,
    "X" : 10,
    "XL" : 40,
    "L" : 50,
    "XC" : 90,
    "C" : 100,
    "CD" : 400,
    "D" : 500,
    "CM" : 900,
    "M" : 1000,
}

def romanToInt(s):
    total = 0
    skip = False
    skip2 = False
    for i in range(0, len(s)):
        if skip == False:
            if i < len(s) - 1:
                gurjap = s[i] + s[i + 1]
                if gurjap in dict.keys():
                    total += dict[gurjap]
                    skip = True
                    skip2 = True
            if skip2 == False:
                if i <= len(s):
                    gorav = s[i]
                    total += dict[gorav]
        else:
            skip = False
            skip2 = False
    return total

word = "MM"
print(romanToInt(s= word))