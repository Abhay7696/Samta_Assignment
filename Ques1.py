#Task 1: Calculate Area with Conditions Write a Python function calculate_area that takes two parameters: length and width. It should calculate and return the area of a rectangle. However, add a condition: if the length is equal to the width, return "This is a square!" instead of the area. Then, write a program to input values for length and width from the user and call the calculate_area function to display either the area or the message.

def calculate_area(length, width):
    if length == width:
        return "This is a square!"
    else:
        return length * width

length_input = float(input("Enter the length: "))
width_input = float(input("Enter the width: "))

result = calculate_area(length_input, width_input)
if isinstance(result, str):
    print(result)
else:
    print(f"The area of the rectangle is {result} square units.")
