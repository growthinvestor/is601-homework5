from calculator.calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, ModulusCommand, ExponentiateCommand

def calculate_and_print(a_string=None, b_string=None, operation_string=None):
    calc = Calculator()

    if a_string is not None and b_string is not None and operation_string is not None:
        try:
            a = float(a_string)
            b = float(b_string)

            # Creating commands based on the operation
            if operation_string == 'add':
                command = AddCommand(a, b)
            elif operation_string == 'subtract':
                command = SubtractCommand(a, b)
            elif operation_string == 'multiply':
                command = calc.create_command('multiply_plugin', a, b)
            elif operation_string == 'divide':
                if b == 0:
                    print("An error occurred: Cannot divide by zero.")
                    return
                command = calc.create_command('divide_plugin', a, b)
            elif operation_string == 'modulus':
                command = ModulusCommand(a, b)
            elif operation_string == 'exponentiate':
                command = ExponentiateCommand(a, b)
            else:
                print(f"Unknown operation: {operation_string}.")
                return
            
            result = calc.compute(command)

            # Ensure consistent output formatting without decimal points for whole numbers
            result_str = str(int(result)) if result.is_integer() else str(result)

            print(f"The result of {a} {operation_string} {b} is equal to {result_str}.")
        except ValueError:
            print(f"Invalid number input: {a_string} or {b_string} is not a valid number.")
    else:
        # Existing code for interactive mode
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
                result_str = f"{result:.0f}" if result.is_integer() else str(result)
                print(f"Result: {result_str}")

            elif choice == '3':
                calc.load_plugin('multiply_plugin')
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                multiply_command = calc.create_command('multiply_plugin', a, b)
                result = calc.compute(multiply_command)
                result_str = f"{result:.0f}" if result.is_integer() else str(result)
                print(f"Result: {result_str}")

            elif choice == '4':
                calc.load_plugin('divide_plugin')
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                if b == 0:
                    print("An error occurred: Cannot divide by zero.")
                    continue
                divide_command = calc.create_command('divide_plugin', a, b)
                result = calc.compute(divide_command)
                result_str = f"{result:.0f}" if result.is_integer() else str(result)
                print(f"Result: {result_str}")

            elif choice == '5':
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                command = ModulusCommand(a, b)
                result = calc.compute(command)
                result_str = f"{result:.0f}" if result.is_integer() else str(result)
                print(f"Result: {result_str}")

            elif choice == '6':
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                command = ExponentiateCommand(base, exponent)
                result = calc.compute(command)
                result_str = f"{result:.0f}" if result.is_integer() else str(result)
                print(f"Result: {result_str}")

            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    calculate_and_print()
