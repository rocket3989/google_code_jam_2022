for tc in range(int(input())):
    
    R, C = [int(x) for x in input().split()]


    r1 = '+-' * C + '+'
    r2 = '|.' * C + '|'

    print(f"Case #{tc + 1}:")

    print('..' + r1[2:])
    print('..' + r2[2:])

    for _ in range(R - 1):
        print(r1)
        print(r2)

    print(r1)