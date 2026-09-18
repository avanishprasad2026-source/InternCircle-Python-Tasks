def calculator():
    print("--- Simple Calculator ---")
    print("Operations: +, -, *, /")
    op = input("Enter operator (+, -, *, /): ")
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if op == '+':
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
                print("Invalid operator entered.")
    except ValueError:
        print("Error: Please enter valid numerical values.")

def unit_converter():
    print("\n--- Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    choice = input("Choose conversion (1 or 2): ")
    
    try:
        if choice == '1':
            km = float(input("Enter value in kilometers: "))
            miles = km * 0.621371
            print(f"{km} km is equal to {miles:.2f} miles")
        elif choice == '2':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    calculator()
    print("\n")
    unit_converter()
