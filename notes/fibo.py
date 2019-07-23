def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(7))

def fib_loop(n):
    if n == 1 or n == 0:
        return 1
    else:
        ans = 1
        noans = 1
        for i in range(1,n):
            ans , noans = noans + ans , ans
    
    return ans
    
print(fib_loop(7))