import math 

def paint_calc(heigth, width, cover):
    num_cans = (heigth * width / cover)
    round_up_cans = math.ceil(num_cans)
    print(f"You need {round_up_cans} cans of paint")


test_h = int(input())
test_w = int(input())

coverage = 5
paint_calc(heigth=test_h,width=test_w, cover=coverage)