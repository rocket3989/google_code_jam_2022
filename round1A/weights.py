# running out of time, I decided to solve just the first tc for this q
# exhaustive search through all possible options

from functools import lru_cache
from collections import Counter


# boilerplate to find permutations
def next_permutation_helper(perm):
    if not perm:
        return perm

    n = len(perm)

    for i in range(n - 1, -1, -1):
        if not perm[i - 1] >= perm[i]:
            break

    k = i - 1

    if k == -1:
        return []

    for i in range(n - 1, k, -1):
        if not perm[k] >= perm[i]:
            perm[i], perm[k] = perm[k], perm[i]
            break

    perm[k + 1 :] = reversed(perm[k + 1 :])

    return perm

def multiset_permutation(A):
    A = sorted(A)
    result = list()

    while True:
        result.append(A.copy())
        A = next_permutation_helper(A)
        if not A:
            break

    return result




for tc in range(int(input())):
    
    E, W = [int(x) for x in input().split()]

    count = 0

    arr = []
    
    for _ in range(E):
        arr.append([int(x) for x in input().split()])


    # exhaustive search of all ways to stack weights 
    @lru_cache(maxsize=None)
    def search(pos, stack, E, W):
        state = Counter(stack)

        # figure out what weights need to be added
        need = []
        for i in range(W):
            need.extend([i] * (arr[pos][i] - state[i]))
        
        cost = len(need)

        if pos == E - 1:
            return cost + sum(arr[-1])
        
        best = float('inf')

        # iterate through all ways of adding needed weights
        for perm in multiset_permutation(need):
            curr = list(stack) + perm
            state = Counter(curr)

            over = Counter()

            for k, v in state.items():
                if v > arr[pos + 1][k]:
                    over[k] += v - arr[pos + 1][k]
            rem = 0

            # remove weights that can't be used by next person
            while over:
                el = curr.pop()
                rem += 1
                if el in over:
                    over[el] -= 1
                    if over[el] == 0:
                        over.pop(el)

            # try all possible ways of passing the weights, removing one at a time
            for i in range(len(curr) + 1):    
                score = rem + i + search(pos + 1, tuple(curr[:len(curr) - i]), E, W)
                best = min(best, score)

        return best + cost

        


    print(f"Case #{tc + 1}: {search(0, (), E, W)}")