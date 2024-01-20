#ask for parameters from the user
square = float(input("What is the length of a side of the square? "))
square_area = f' The area of the square is: {square*4}'
print(square_area)

rect_l = float(input("What is the length of rectangle? "))
rect_w = float(input("What is the width of the rectangle? "))
rect_area = f' The area of the rectangle is: {rect_l * rect_w}'
print(rect_area)

cir_rad = float(input("What is the radius of the circle? "))
cir_area = f' The area of the circle is: {3.14 * cir_rad ** 2}'
print(cir_area)
