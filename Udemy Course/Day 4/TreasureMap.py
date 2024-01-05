line1 = [" "," "," "]
line2 = [" "," "," "]
line3 = [" "," "," "]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot")
position = input()
####################

letter = position[0].lower()

abc = ["a","b","c"]

Letterindex = abc.index(letter)
numindex = int(position[1]) - 1

map[numindex][Letterindex] = "X"

####################
print(f"{line1}\n{line2}\n{line3}\n")

