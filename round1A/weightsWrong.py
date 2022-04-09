# attempt at solving full points for the weights question. I think my solution was flawed

# the idea was, find the xor between each person, adding to a counter for each weight not in the xor
# build those xor values into another array, and reduce

for tc in range(int(input())):
    
    E, W = [int(x) for x in input().split()]

    count = 0

    # arr = [[0 for _ in range(W)]] 
    arr = []

    for _ in range(E):
        arr.append([int(x) for x in input().split()])

    first = True
    layer = 1
    while arr:
        print(arr)
        next_arr = []
        for a, b in zip(arr, arr[1:]):
            curr = []
            costl = 0
            costr = 0
            for x, y in zip(a, b):
                curr.append(min(x, y))
                costl += (x - curr[-1])
                costr += (y - curr[-1]) 
            
            print(costl, costr, layer, a, b)
            
            count += costl

            if first:
                count += costr

            next_arr.append(curr)
        
        if first:
            print('x', sum(b), sum(arr[0]))
            count += sum(arr[0])
            count += sum(b)
            first = False
        layer += 1
        arr = next_arr

    print(f"Case #{tc + 1}: {count}")