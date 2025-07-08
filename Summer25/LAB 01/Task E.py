def main():
    import sys
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))
    
    if n == 1:
        print("YES")
    elif n == 2:
        if a[0] <= a[1]:
            print("YES")
        else:
            print("NO")
    else:
        even = []
        odd = []
        for i in range(n):
            if i % 2 == 0:
                even.append(a[i])
            else:
                odd.append(a[i])
                
        even.sort()
        odd.sort()
        
        b = []
        index_even = 0
        index_odd = 0
        for i in range(n):
            if i % 2 == 0:
                b.append(even[index_even])
                index_even += 1
            else:
                b.append(odd[index_odd])
                index_odd += 1
                
        is_sorted = True
        for i in range(1, n):
            if b[i] < b[i-1]:
                is_sorted = False
                break
                
        print("YES" if is_sorted else "NO")

if __name__ == "__main__":
    main()
