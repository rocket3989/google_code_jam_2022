# code does not pass

import random
for tc in range(int(input())):
    N, K = [int(x) for x in input().split()]

    room, count = [int(x) for x in input().split()]

    known = [count]

    poss = [i for i in range(1, N + 1) if i != room]

    random.shuffle(poss)

    # choose k random rooms to visit, build guess based on passages
    for r in poss[:K]:
        print(f'T {r}')

        r, c = [int(x) for x in input().split()]

        known.append(c)

    guess = (sum(known) * N) / (2 * len(known))

    guess /= 1.00012 # constant found with experimentation 

    print(f"E {round(guess)}")