def fibo_series_sum(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibo_series_sum(n-1) + fibo_series_sum(n-2)
    

print(fibo_series_sum(20))