def serie(n,a,b):
    if n==0:
        return a
    if n==1:
        return b
    n = 3(n-1)+2(n+5)
    serie(n,a,b)
assert serie(0,5,8) == 5