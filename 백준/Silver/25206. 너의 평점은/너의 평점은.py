import sys
input=sys.stdin.readline
grade={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
total=0.0
cred_sum=0.0
for _ in range(20):
    subj,cred,gra=input().split()
    cred=float(cred)
    if gra!='P':
        cred_sum+=cred
        total+=cred*grade[gra]
print(total/cred_sum if cred_sum else 0)
