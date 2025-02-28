T = int(input())
for i in range(T): 
    inp = input()
    line = inp[10:]
    parts = line.split( )
    num1 = parts[0]
    opt = parts[1]
    num2 = parts[2]
    rslt = 0

    if opt == '+': 
        rslt = int(num1) + int(num2)
        print(f'{rslt:.6f}')
    elif opt == '-': 
        rslt = int(num1) - int(num2)
        print(f'{rslt:.6f}')
    elif opt == '*': 
        rslt = int(num1) * int(num2)
        print(f'{rslt:.6f}')
    elif opt == '/':
        rslt = int(num1) / int(num2)
        print(f'{rslt:.6f}')