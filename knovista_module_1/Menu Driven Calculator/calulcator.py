import math

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 10:
            break
        elif choice in (1, 2, 3, 4, 5):
            n1 = float(input("Enter first number: "))
            n2 = float(input("Enter second number: "))

            if choice == 1:
                result = n1 + n2
            elif choice == 2:
                result = n1 - n2
            elif choice == 3:
                result = n1 * n2
            elif choice == 4:
                result = n1 / n2
            else:
                result = n1 ** n2

            print("Result:", result)
        elif choice == 6:
            n = float(input("Enter a number: "))
            print("Result:", math.sqrt(n))
        elif choice in (7, 8, 9):
            angle = math.radians(float(input("Enter angle in degrees: ")))
            if choice == 7:
                result = math.sin(angle)
            elif choice == 8:
                result = math.cos(angle)
            else:
                result = math.tan(angle)
            print("Result:", result)
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter valid numbers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except (OverflowError, ValueError):
        print("The operation is not valid for the given numbers.")
