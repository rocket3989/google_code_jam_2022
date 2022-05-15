from heapq import heappop, heappush


for tc in range(int(input())):
    n, c = [int(x) for x in input().split()]

    l0, l1, r0, r1 = [], [], [], []

    for _ in range(n):
        x, s = [int(x) for x in input().split()]

        if x > 0:
            if s:
                r1.append(x)
            else:
                r0.append(x)
        
        else:
            if s:
                l1.append(-x)
            else:
                l0.append(-x)


    def solve(x, y, c):
        x.sort()
        y.sort()


        n = len(x)
        m = len(y)

        h = [(0, 0, 0)]

        seen = set()

        while h:
            cost, xpos, ypos = heappop(h)

            # print(cost, xpos, ypos)

            if xpos == n and ypos == m:
                return cost

            if (xpos, ypos) in seen:
                continue

            seen.add((xpos, ypos))

            options = []

            for i in range(2):
                if xpos + i < n:
                    options.append((x[xpos + i], 0))

                if ypos + i < m:
                    options.append((y[ypos + i], 1))

            options.sort()


            if options[0][1] == 1:
                heappush(h, (cost + 2 * options[0][0], xpos, ypos + 1))
            else:
                heappush(h, (cost + 2 * options[0][0], xpos + 1, ypos))

            if xpos < n and ypos < m:
                heappush(h, (cost + 2 * max(x[xpos], y[ypos]), xpos + 1, ypos + 1))
            
            if len(options) == 1 or options[0][1] != options[1][1]:
                continue
                
            if options[0][1]:
                heappush(h, (cost + 2 * max(y[ypos], y[ypos + 1]) + c, xpos, ypos + 2))
            
            else:
                heappush(h, (cost + 2 * max(x[xpos], x[xpos + 1]) + c, xpos + 2, ypos))




    print(f"Case #{tc + 1}: {solve(l0, l1, c) + solve(r0, r1, c)}")







