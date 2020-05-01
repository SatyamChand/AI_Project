s=5
n=5
rolls=[]
for i in range(n):
    name="Class"+str(i+1)
    roll=list(range(1001+i*s,1001+(i+1)*s))
    #print(name,' ',roll)
    rolls.extend(list((i,name)for i in roll))
print(rolls)

rollz=[]
for i in range(n):
    name="Class"+str(i+1)
    roll=list((range(1001+i*s,1001+(i+1)*s)))
    rollz.extend(list((i,name)for i in range(1001+i*s,1001+(i+1)*s)))
print(rollz)