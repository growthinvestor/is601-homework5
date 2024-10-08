# IS-601 Homework 5
# Performed Testing Using input data, plugins and commands
# Added additional functions Modulus and Exponentiate both are test successfully
# Cleared all errors and fixed issues

(myenv) ajaswal@AJ:~/projects/homework5$ python main.py

Options:
1. Add
2. Subtract
3. Multiply (using plugin)
4. Divide (using plugin)
5. Modulus
6. Exponentiate
7. Exit
Choose an option (1-7): 1
Enter the first number: 4
Enter the second number: 707
Result: 711

Options:
1. Add
2. Subtract
3. Multiply (using plugin)
4. Divide (using plugin)
5. Modulus
6. Exponentiate
7. Exit
Choose an option (1-7): 3
Enter the first number: 10
Enter the second number: 9
Result: 90

Options:
1. Add
2. Subtract
3. Multiply (using plugin)
4. Divide (using plugin)
5. Modulus
6. Exponentiate
7. Exit
Choose an option (1-7): 5
Enter the first number: 7
Enter the second number: 9
Result: 7

Options:
1. Add
2. Subtract
3. Multiply (using plugin)
4. Divide (using plugin)
5. Modulus
6. Exponentiate
7. Exit
Choose an option (1-7): 6
Enter the base: 45
Enter the exponent: 4
Result: 4100625

Options:
1. Add
2. Subtract
3. Multiply (using plugin)
4. Divide (using plugin)
5. Modulus
6. Exponentiate
7. Exit
Choose an option (1-7): 7
Exiting the calculator. Goodbye!

# Coverage

platform linux -- Python 3.10.12, pytest-8.2.0, pluggy-1.5.0 -- /home/ajaswal/projects/homework3/myenv/bin/python3
cachedir: .pytest_cache
rootdir: /home/ajaswal/projects/homework5
configfile: pytest.ini
testpaths: tests
plugins: Faker-30.1.0, pylint-0.21.0, cov-5.0.0
collected 42 items                                                                                                                                         
tests/test_calculation.py::test_calculation_operations[a0-b0-exponentiate-expected0] PASSED                                                          [  2%]
tests/test_calculation.py::test_calculation_operations[a1-b1-modulus-expected1] PASSED                                                               [  4%]
tests/test_calculation.py::test_calculation_operations[a2-b2-divide-expected2] PASSED                                                                [  7%]
tests/test_calculation.py::test_calculation_operations[a3-b3-add-expected3] PASSED                                                                   [  9%]
tests/test_calculation.py::test_calculation_operations[a4-b4-multiply-expected4] PASSED                                                              [ 11%]
tests/test_calculation.py::test_find_by_operation PASSED                                                                                             [ 14%]
tests/test_calculation.py::test_divide_by_zero PASSED                                                                                                [ 16%]
tests/test_calculation.py::test_modulus_operation PASSED                                                                                             [ 19%]
tests/test_calculation.py::test_exponentiate_operation PASSED                                                                                        [ 21%]
tests/test_calculations.py::test_add_calculation PASSED                                                                                              [ 23%]
tests/test_calculations.py::test_get_history PASSED                                                                                                  [ 26%]
tests/test_calculations.py::test_clear_history PASSED                                                                                                [ 28%]
tests/test_calculations.py::test_get_latest PASSED                                                                                                   [ 30%]
tests/test_calculations.py::test_find_by_operation PASSED                                                                                            [ 33%]
tests/test_calculations.py::test_get_latest_with_empty_history PASSED                                                                                [ 35%]
tests/test_calculator.py::test_add_command PASSED                                                                                                    [ 38%]
tests/test_calculator.py::test_subtract_command PASSED                                                                                               [ 40%]
tests/test_calculator.py::test_multiply_plugin PASSED                                                                                                [ 42%]
tests/test_calculator.py::test_divide_plugin PASSED                                                                                                  [ 45%]
tests/test_calculator.py::test_divide_by_zero PASSED                                                                                                 [ 47%]
tests/test_calculator.py::test_modulus_command PASSED                                                                                                [ 50%]
tests/test_calculator.py::test_exponentiate_command PASSED                                                                                           [ 52%]
tests/test_main.py::test_main[5-3-add-The result of 5.0 add 3.0 is equal to 8] PASSED                                                                [ 54%]
tests/test_main.py::test_main[10-2-subtract-The result of 10.0 subtract 2.0 is equal to 8] PASSED                                                    [ 57%]
tests/test_main.py::test_main[4-5-multiply-The result of 4.0 multiply 5.0 is equal to 20] PASSED                                                     [ 59%]
tests/test_main.py::test_main[20-4-divide-The result of 20.0 divide 4.0 is equal to 5] PASSED                                                        [ 61%]
tests/test_main.py::test_main[1-1-divide-The result of 1.0 divide 1.0 is equal to 1] PASSED                                                          [ 64%]
tests/test_main.py::test_main[1-0-divide-An error occurred: Cannot divide by zero.] PASSED                                                           [ 66%]
tests/test_main.py::test_main[9-3-modulus-The result of 9.0 modulus 3.0 is equal to 0] PASSED                                                        [ 69%]
tests/test_main.py::test_main[10-3-modulus-The result of 10.0 modulus 3.0 is equal to 1] PASSED                                                      [ 71%]
tests/test_main.py::test_main[2-3-exponentiate-The result of 2.0 exponentiate 3.0 is equal to 8] PASSED                                              [ 73%]
tests/test_main.py::test_main[3-0-exponentiate-The result of 3.0 exponentiate 0.0 is equal to 1] PASSED                                              [ 76%]
tests/test_main.py::test_main[9-3-unknown-Unknown operation: unknown.] PASSED                                                                        [ 78%]
tests/test_main.py::test_main[a-3-add-Invalid number input: a or 3 is not a valid number.] PASSED                                                    [ 80%]
tests/test_main.py::test_main[5-b-subtract-Invalid number input: 5 or b is not a valid number.] PASSED                                               [ 83%]
tests/test_operations.py::test_operation_add PASSED                                                                                                  [ 85%]
tests/test_operations.py::test_operation_subtract PASSED                                                                                             [ 88%]
tests/test_operations.py::test_operation_multiply PASSED                                                                                             [ 90%]
tests/test_operations.py::test_operation_divide PASSED                                                                                               [ 92%]
tests/test_operations.py::test_divide_by_zero PASSED                                                                                                 [ 95%]
tests/test_operations.py::test_operation_modulus PASSED                                                                                              [ 97%]
tests/test_operations.py::test_operation_exponentiation PASSED    