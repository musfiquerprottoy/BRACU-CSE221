T = int(input()) 

for i in range(T): 
    inp = input().split()
    num1 = float(inp[1])
    opd = inp[2]
    num2 = float(inp[3])
    rslt = 0

    if opd == '+': 
        rslt = num1 + num2
    elif opd == '-': 
        rslt = num1 - num2
    elif opd == '*': 
        rslt = num1 * num2
    elif opd == '/':
        rslt = num1 / num2 
    print(f'{rslt:.6f}')
