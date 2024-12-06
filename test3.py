#Gcd các số từ x đến x+n-1
def sub4(x, n):
    # Tính tổng các ước cho các số từ x đến x + n - 1
    result = [0] * n
    for i in range(1, int((x + n - 1) ** 0.5) + 1):
        for j in range(max((x // i) * i, i * i), x + n, i):
            if j >= x:
                result[j - x] += i
                if j // i != i:
                    result[j - x] += j // i
    return result
print(sub4(4,6))