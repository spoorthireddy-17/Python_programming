def primes_upto(n):
    for num in range(2, n+1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

n=int(input('enter n:'))
primes_upto(n)
