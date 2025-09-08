import sys
input=sys.stdin.readline
n=int(input())
cards=set(map(int,input().split()))
m=int(input())
query=list(map(int,input().split()))
print(' '.join('1' if x in cards else '0' for x in query))
