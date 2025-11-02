print('==================')
print('Area Calculator')
print('==================')

shape = int(input("""
1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit
                  
Which Shape: """))

if shape == 1:
    height = float(input('Height: '))
    base = float(input('Base: '))
    area = (height * base) / 2
elif shape == 2:
    length = float(input('Length: '))
    width = float(input('Width: '))
    area = length * width
elif shape == 3:
    side = float(input('Side: '))
    area = side ** 2 
elif shape == 4:
    radius = float(input('Radius: '))
    area = 3.14 * radius ** 2
elif shape == 5:
    print('Goodbye!')
    quit()
else:
    print('Invalid input')
    quit()



print('The area is:', area)