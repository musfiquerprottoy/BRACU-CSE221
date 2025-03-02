stdns = int(input())
ids = list(map(int, input().split())) 
marks = list(map(int, input().split()))  

def selectionSort(marks, ids, stdns): 
    count = 0
    output_lines = []

    for i in range(stdns): 
        max_id = i
        for j in range(i+1, stdns): 
            if marks[j] > marks[max_id]: 
                max_id = j
            elif marks[j] == marks[max_id]: 
                if ids[j] < ids[max_id]: 
                    max_id = j
        
        if max_id != i: 
            marks[i], marks[max_id] = marks[max_id], marks[i]
            ids[i], ids[max_id] = ids[max_id], ids[i]
            count += 1

        output_lines.append(f"ID: {ids[i]} Mark: {marks[i]}\n")  

    print(f'Minimum swaps: {count}')
    print("".join(output_lines), end="") 

selectionSort(marks, ids, stdns)  