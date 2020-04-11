from Circle import Circle

def main():
    #Create a Circle object with radius 1
    myCircle = Circle()

    # print areas for radius 1, 2, 3, 4 and 5
    n = 5
    printAreas(myCircle, n)

    # Display myCircle.radius and times
    print("\nRadius is", myCircle.getRadius())
    print("n is", n)


# print a table of areas for radius
def printAreas(c, times):
    print("Radius \t\tArea")
    while times >=1:
        print(c.getRadius(), "\t\t", c.getArea())
        c.setRadius(c.getRadius() + 1)
        times = times - 1

main()

