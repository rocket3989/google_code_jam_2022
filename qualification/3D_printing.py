for tc in range(int(input())):
    
    p = []

    for _ in range(3):
        p.append([int(x) for x in input().split()])

    mins = [min(p[j][i] for j in range(3)) for i in range(4)]

    total = 10 ** 6

    ans = []

    for val in mins:
        ink = min(total, val)
        ans.append(str(ink))
        total -= ink

    if total:
        print(f"Case #{tc + 1}: {'IMPOSSIBLE'}")

    else:
        print(f"Case #{tc + 1}: {' '.join(ans)}")