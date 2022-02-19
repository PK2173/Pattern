def q(a,b):
    if (a)==(b):
        print()
        return 
    else:
        print((a+1),end=" ")
        q((a+1),b)  

def p(n):
    global s
    if n==0:
        return 1
    else:
        p(n-1)
        s=(s+n)
        q((s-n),s)

s=0
n=int(input())
p(n)