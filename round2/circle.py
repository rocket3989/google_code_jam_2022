import math

last = 0
for r in range(100):
    ans = 0

    # r = int(input())

    mat1 = [[0 for _ in range(2* r + 1)] for _ in range(2 * r + 1)]
    mat2 = [[0 for _ in range(2* r + 1)] for _ in range(2 * r + 1)]

    for x in range(-r, r + 1):
        for y in range(-r, r + 1):
            if round(math.sqrt(x * x + y * y)) <= r:
                mat1[r + x][r + y] = 1

    
    for R in range(r + 1):
        for x in range(-R, R + 1):
            y = round(math.sqrt(R * R - x * x))


            mat2[r + x][r + y] = 1
            mat2[r + x][r - y] = 1
            mat2[r + y][r + x] = 1
            mat2[r - y][r + x] = 1




    for i in range(2*r + 1):
        for j in range(2*r + 1):
            if mat1[i][j] != mat2[i][j]:
                ans += 1

    ans //= 4

    print(ans - last)
    
    last = ans



    # print(f"Case #{tc + 1}: {ans}")

