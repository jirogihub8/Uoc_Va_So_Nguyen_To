#Gcd 1 so
def gcd(x):
    s=0
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            s+=i
            if x//i!=i:
                s+=x//i
    return s
print(gcd(10))