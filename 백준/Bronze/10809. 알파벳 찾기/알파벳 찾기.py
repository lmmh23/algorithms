import sys
s=sys.stdin.readline().strip()
res=[-1]*26
for i,ch in enumerate(s):
    idx=ord(ch)-97
    if res[idx]==-1:
        res[idx]=i
print(' '.join(map(str,res)))
