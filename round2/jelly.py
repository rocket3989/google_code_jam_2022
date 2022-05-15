from itertools import permutations


for tc in range(int(input())):
    n = int(input())

    children = []

    for i in range(n):
        children.append([int(x) for x in input().split()])

    candy = []

    special = [int(x) for x in input().split()]

    for i in range(n):
        candy.append([int(x) for x in input().split()])

    for perm in permutations(range(n)):
        c = [special] + candy[:]

        out = []
        for child in perm:
            best = 0
            best_dist = float('inf')
            j, k = children[child]
            for i, (x, y) in reversed(list(enumerate(c))):

                dist = (x - j) * (x - j) + (y - k) * (y - k)
                if dist < best_dist:
                    best = i
                    best_dist = dist
            
            if best == 0:
                break

            out.append((child + 1, best + 1))

            c[best] = (float('inf'), float('inf'))

        else:
            print(f"Case #{tc + 1}: POSSIBLE")
            for row in out:
                print(*row)
            break
    else:
        print(f"Case #{tc + 1}: IMPOSSIBLE")










    

