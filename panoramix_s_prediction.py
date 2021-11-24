primes = [2]

def divisible_by_prime(n):
    global primes
    for prime in primes:
        if n % prime == 0:
            return False
    return True

n, m = list(map(int, input().split()))

for i in range(3, 54):
    if divisible_by_prime(i):
        primes.append(i)

index = primes.index(n)
print("YES") if primes[index + 1] == m else print("NO")