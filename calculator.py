import math

def main():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Modulus")
        print("7. Square Root")
        print("8. Power (x^y)")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == "9":
            print("Calculator closed.")
            break

        elif choice in ["1", "2", "3", "4", "6"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result = {num1 + num2}")

            elif choice == "2":
                print(f"Result = {num1 - num2}")

            elif choice == "3":
                print(f"Result = {num1 * num2}")

            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                else:
                    print(f"Result = {num1 / num2}")

        elif choice == "5":
            num = float(input("Enter a number: "))
            print("Square =", num ** 2)

        elif choice == "6":
                print(f"Result = {num1 % num2}")

        elif choice == "7":
            num = float(input("Enter a number: "))

            if num < 0:
                print("Error: Square root of a negative number is not possible.")
            else:
                print("Square Root =", math.sqrt(num))

        elif choice == "8":
            base = float(input("Enter base (x): "))
            exponent = float(input("Enter exponent (y): "))
            print("Result =", base ** exponent)

        else:
            print("Invalid choice! Please enter a number between 1 and 9.")

main()
