# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A

n = int(input())

prime_count = [0] * (n + 1)

for i in range(2, n+1):
    if prime_count[i] == 0:
        for j in range(i, n+1, i):
            prime_count[j] += 1 

# print(prime_count)
almost_prime_count = sum(1 for count in prime_count if count == 2)
print(almost_prime_count)