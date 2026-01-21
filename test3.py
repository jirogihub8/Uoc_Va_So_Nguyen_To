def sub4(x, n):
    res = [0] * n
    R =  x + n- 1

    for i in range(1, int(R**0.5) + 1):
        start = ((x + i - 1) // i) * i
        for j in range(start, R+1, i):
            if j < i * i:
                continue

            if i != j:
                res[j - x] += i
            d = j // i
            if d != i and d != j:
                res[j - x] += d

    return res
