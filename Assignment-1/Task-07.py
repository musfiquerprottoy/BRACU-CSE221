N = int(input())
trains = [input().strip() for _ in range(N)]

for i in range(N):
    for j in range(N-i-1):
        fline =  trains[j].split()
        sline = trains[j+1].split()

        if fline[0] > sline[0]: 
            trains[j], trains[j+1] = trains[j+1], trains[j]
        elif fline[0] == sline[0] and fline[-1] < sline[-1]:
            trains[j], trains[j+1] = trains[j+1], trains[j]
        
for train in trains: 
    print(train)
    