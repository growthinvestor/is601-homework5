from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, ModulusCommand, ExponentiateCommand

def main():
    calc = Calculator()
    
    while True:
        print("\nOptions:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply (using plugin)")
        print("4. Divide (using plugin)")
        print("5. Modulus")
        print("6. Exponentiate")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2']:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
        
            if choice == '1':
                command = AddCommand(a, b)
            elif choice == '2':
                command = SubtractCommand(a, b)
            result = calc.compute(command)
            print(f"Result: {result}")

        elif choice == '3':
            calc.load_plugin('multiply_plugin')
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            multiply_command = calc.create_command('multiply_plugin', a, b)
            result = calc.compute(multiply_command)
            print(f"Result: {result}")

        elif choice == '4':
            calc.load_plugin('divide_plugin')
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            divide_command = calc.create_command('divide_plugin', a, b)
            result = calc.compute(divide_command)
            print(f"Result: {result}")

        elif choice == '5':
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            command = ModulusCommand(a, b)
            result = calc.compute(command)
            print(f"Result: {result}")

        elif choice == '6':
            base = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            command = ExponentiateCommand(base, exponent)
            result = calc.compute(command)
            print(f"Result: {result}")

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
