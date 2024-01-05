import math

def paint_calc(height, width, cover):
    num_of_can = math.ceil((height * width) / cover)
    print(f"You'll need {num_of_can} cans of paint.")
###########################
test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height = test_h, width= test_w, cover = coverage)