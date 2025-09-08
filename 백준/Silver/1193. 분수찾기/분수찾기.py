n=int(input())
line=1
while n>line:
    n-=line
    line+=1
if line%2==0:
    num=n
    den=line-n+1
else:
    num=line-n+1
    den=n
print(f"{num}/{den}")
