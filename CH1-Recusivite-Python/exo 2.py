def syracuse (n):
    if n == 1:
        print ("stop")
    elif n % 2 == 0:
        n = n/2
        syracuse(n)
    elif n % 2 == 1:
        n = 3*n+1
        syracuse(n)