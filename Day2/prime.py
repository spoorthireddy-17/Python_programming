#to check given number is prime or not

def check(num):
    if num > 1:
        i = 2
        is_prime = True
        while i * i <= num:   # check divisors up to √num
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            return "Prime"
        else:
            return "Not Prime"
    else:
       return"Not Prime"
    
n=int(input('enter n:'))
res=check(n)
print(res)