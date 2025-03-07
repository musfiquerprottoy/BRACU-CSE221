def mergelist():
    N = int(input().strip())
    Alice = list(map(int, input().strip().split()))

    M = int(input().strip())
    Bob = list(map(int, input().strip().split()))

    i, j = 0, 0
    merged_list = []

    while i<N and j<M: 
        if Alice[i]<= Bob[j]:
            merged_list.append(Alice[i])
            i += 1
        else: 
            merged_list.append(Bob[j])
            j += 1

    while i<N: 
        merged_list.append(Alice[i])
        i += 1

    while j<M: 
        merged_list.append(Bob[j])
        j += 1

    print(" ".join(map(str, merged_list)))

mergelist() 