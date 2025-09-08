s=input().strip()
for rep in ["dz=","c=","c-","d-","lj","nj","s=","z="]:
    s=s.replace(rep,"*")
print(len(s))
