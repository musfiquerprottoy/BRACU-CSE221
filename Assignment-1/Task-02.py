T = int(input())  # Number of test cases

for i in range(T): 
    inp = input().split()  # Split the input into parts
    num1 = float(inp[1])  # First number
    opt = inp[2]  # Operator (+, -, *, /)
    num2 = float(inp[3])  # Second number
    rslt = 0

    # Perform the calculation
    if opt == '+': 
        rslt = num1 + num2
    elif opt == '-': 
        rslt = num1 - num2
    elif opt == '*': 
        rslt = num1 * num2
    elif opt == '/':
        rslt = num1 / num2  # Division automatically handles float values

    # Print the result with 6 decimal places
    print(f'{rslt:.6f}')
