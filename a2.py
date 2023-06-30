
def rectangle_area(length, width):
    area = length * width
    return area

def square_area(side):
    area = side ** 2
    return area

def circle_area(radius):
    area = 3.14159 * radius ** 2
    return area

def triangle_area(base, height):
    area = 0.5 * base * height
    return area


print("Choose a shape to find its area:")
print("1. Rectangle")
print("2. Square")
print("3. Circle")
print("4. Triangle")
choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    area = rectangle_area(length, width)
    print("The area of the rectangle is:", area)

elif choice == 2:
    side = float(input("Enter the length of a side of the square: "))
    area = square_area(side)
    print("The area of the square is:", area)

elif choice == 3:
    radius = float(input("Enter the radius of the circle: "))
    area = circle_area(radius)
    print("The area of the circle is:", area)

elif choice == 4:
    base= float(input("Enter the base of the triangle "))
    height = float(input("Enter the height of the tiangle "))
    area = triangle_area(base, height)
    print("The area of the rectangle is:", area)
else:
    print("Wrong Choice")
