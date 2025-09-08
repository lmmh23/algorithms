import sys
n,b=map(int,sys.stdin.readline().split())
res=[]
while n>0:
    n,rem=divmod(n,b)
    if rem>=10:
        res.append(chr(ord('A')+rem-10))
    else:
        res.append(str(rem))
print(''.join(reversed(res)))
