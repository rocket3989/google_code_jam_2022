for tc in range(int(input())):
    n, k = [int(x) for x in input().split()]

    target = (n * n - 1) - k

    if target & 1:
        print(f"Case #{tc + 1}: IMPOSSIBLE")
        continue


    pos = 3
    out = []

    seen = 1

    for ring in range(n, 1, -2):
        
        eights = (ring - 2) // 2

        if target == 0:
            break

        # print(ring, eights)

        if target >= eights * 8 + 6:
            target -= eights * 8 + 6
            out.append((seen + 1, + seen + 2 + eights * 8 + pos * 2))
            break
        for pos in range(3):
            if target == eights * 8 + pos * 2:
                target -= eights * 8 + pos * 2
                out.append((seen + 1 + (3 - pos) * (ring - 1), (3 - pos) * (ring - 1) + seen + 2 + eights * 8 + pos * 2))
                break
        

        seen += ring * 4 - 4

    if target != 0:
        print(target)
        print(f"Case #{tc + 1}: IMPOSSIBLE")
    else:
        print(f"Case #{tc + 1}: {len(out)}")
        for row in out:
            print(*row)




