for tc in range(int(input())):
    
    N = int(input())

    arr = [int(x) for x in input().split()]

    arr.sort()

    pos = 0

    for val in arr:
        if val > pos:
            pos += 1

    print(f"Case #{tc + 1}: {pos}")