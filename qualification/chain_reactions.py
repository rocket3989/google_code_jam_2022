import sys
sys.setrecursionlimit(10**6) # stupid python...

for tc in range(int(input())):
    
    N = int(input())

    arr = [0] + [int(x) for x in input().split()]

    direction = [int(x) for x in input().split()]

    adj = [[] for i in range(N + 1)]

    # invert the graph into a tree rooted at 0
    for i, val in enumerate(direction, 1):
        adj[val].append(i)

    ans = [0]

    def dfs(node):
        smallest = float('inf')
        val = arr[node]

        for other in adj[node]:
            smallest = min(smallest, dfs(other))

        if smallest == float('inf'):
            ans[0] += val
            return val

        if smallest < val:
            ans[0] += val - smallest

        return max(val, smallest)

        
    dfs(0)

    print(f"Case #{tc + 1}: {ans[0]}")