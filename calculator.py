# calculator_basic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")

    choice = input("Enter choice (1/2): ")

    if choice in ['1', '2']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()


 
