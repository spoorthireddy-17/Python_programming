#prime factors of n

def prime_factors(n):
    for i in range(1,n+1):
        if(n%i==0):
            if(prime(i)):
                print(i,end=" ")
    
def prime(num):
    if num > 1:
        i = 2
        is_prime = True
        while i * i <= num:   # check divisors up to √num
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            return True
        else:
            return False
        
n=int(input('enter n:'))
prime_factors(n)