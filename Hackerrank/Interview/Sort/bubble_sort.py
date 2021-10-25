def countSwaps(a):
    # Write your code here
    max = a[-1]
    for i in a:
        if i > max:
            max += 1
            
    if max != a[-1]:
        count = 0
        for i in range(len(a)):
            for j in range(len(a)-1):
                if a[j] > a[i]:
                    temp = a[j]
                    a[j] = a[i]
                    a[i] = temp
            print(a)
            count += 1
    else:
        count = 0
        
    print(f"Array is sorted in {count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")

countSwaps([3,2,1])
        