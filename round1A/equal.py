# if you make sure to have every power of 2 between 1 - 10 ** 9
# then the subset sum approximation of giving an element to the smaller
# pile one at a time is guaranteed to work. Proof left as exercise to reader

options = [2 ** i for i in range(30)]

fodder = list(set(range(1, 200)) - set(options))[:70]

for tc in range(int(input())):
    N = input()

    print(*(options + fodder), sep= ' ')

    arr = [int(x) for x in input().split()]

    a, b = [], []

    for val in arr + fodder + options[::-1]:
        if sum(a) > sum(b):
            b.append(val)
        else:
            a.append(val)

    print(*a)