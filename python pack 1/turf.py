print("enter the length of your field in feet")
length = input()
lengthint = int(length)
print("enter the width of your field in feet")
width = input()
widthint = int(width)
print("enter the cost per sqaure foot of your field")
cost = input()
costint = int(cost)
area = lengthint*widthint
perimeter = lengthint*2+widthint*2
costfield = area*costint
print("")
print("area of the field")
print(area)
print("perimeter of the field")
print(perimeter)
print("cost of the field")
print(costfield)