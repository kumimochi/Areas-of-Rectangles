#The area of a rectangle is the rectangle's length times its width. Write a program that asks for the length and width of two rectangles.
The program should tell the user which rectangle has the greater area, of if the areas are the same.


rectangle1_length = float(input('What is the length of rectangle 1?'))
rectangle1_width = float(input('What is the width of the rectangle 1?'))
rectangle2_length = float(input('What is the length of rectangle 2?'))
rectangle2_width = float(input('What is the width of the rectangle 2?'))

rectanglearea1 = rectangle1_length * rectangle1_width
rectanglearea2 = rectangle2_length * rectangle2_width

if rectanglearea1 > rectanglearea2:
    print('Rectangle 1 has the greater area.')
elif rectanglearea2 > rectanglearea1:
    print('Reactangle 2 has a greater area.')
else:
    print('The areas are the same.')
