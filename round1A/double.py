# think greedy
# double the current letter if it lex. smaller than the next, otherwise don't
# make sure to combine runs of a single letter together

for tc in range(int(input())):
    
    S = input()

    runs = []
    last = ''
    for val in S:
        if val != last:
            runs.append([val,  1])
            last = val

        else:
            runs[-1][1] += 1
    
    ans = []

    for (a, length), (b, _) in zip(runs, runs[1:]):
        if a < b:
            ans.extend([a] * length * 2)
        
        else:
            ans.extend([a] * length)

    # no matter what, do not double the last letter
    ans.extend([runs[-1][0]] * runs[-1][1])



    print(f"Case #{tc + 1}: {''.join(ans)}")
