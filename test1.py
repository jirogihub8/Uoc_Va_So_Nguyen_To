#sang uoc

def sanguoc(x):
    #sum of divisors
    c=[1]*(x+3)
    for i in range(2,int(x**0.5)+1):
        for j in range(i*i,x+1,i):
            c[j]+=i
            if i*i!=j:
                c[j]+=j//i

    #sum of proper divisors
    for i in range(2,x+1):
        c[i]+=i
    return c
print(sanguoc(10))