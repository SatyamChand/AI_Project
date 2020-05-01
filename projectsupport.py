from simpleai.search import CspProblem, backtrack
import copy

Subs={}
crsr=None
 
def assign_days(Day_arrangement,cursor):
    global Subs
    global crsr
    crsr=cursor;
    cursor.execute('''
    	select sname,count(roll) from Classes,Subjects 
    	where Classes.class=Subjects.class 
    	group by sname 
    	''')
    subs=cursor.fetchall()
    Subs=[]
    for i in subs:
    	print(i)
    	Subs.append(i[0])
    Arrangement=dict((sub,[1,2,3,4,5,6,7]) for sub in Subs)
    print(Arrangement)
    Constraints=[
        (Subs,day_check)
    ]
    Problem=CspProblem(Subs,Arrangement,Constraints)
    output=backtrack(Problem)
    #print(output)
    for y,z in output.items():
        print('Day ',z,'==>',y)
        if z not in Day_arrangement:
            Day_arrangement[z]=[]
        Day_arrangement[z].append(y)
    #print(Day_arrangement)


def day_check(sub,day):
    #print(len(sub))
    global crsr
    #print(sub,day)
    temp=[]
    #rsr.execute('''select * from Subjects''')
    #for j,k in crsr.fetchall():
    #		print(j,k)
    for i in range(len(sub)):
    	#print(sub[i])
    	crsr.execute("""select * from Subjects where sname=='{}'""".format(sub[i]))
    	temp.append([])
    	for j,k in crsr.fetchall():
    		temp[i].append(k)
    for i in range(len(temp)-1):
    	for j in range(i+1,len(temp)):
    		#print(temp[i],' ',temp[j])
    		for k in temp[i]:
    			if k in temp[j] and day[i]==day[j]:
    				#print('clash in ',sub[i],',',sub[j])
    				return 0
    return 1


def arrangement(Seat,Seats,Day_arrangement):
	global crsr
	Subs=[]
	Size=[]
	for i in Day_arrangement:
		print(Day_arrangement[i])
		Subs.append(Day_arrangement[i])
		Seats.append(copy.deepcopy(Seat))

		temp_size=[]
		for j in Day_arrangement[i]:
			crsr.execute('''select sname,count(*) from Subjects,Classes
				where Subjects.class=Classes.class and sname="{}"'''.format(j))
			for x,y in crsr.fetchall():
				if y>(len(Seat)+1)//2:
					print("not possible")
					return 1
				temp_size.append(y)
		temp_sum=sum(temp_size)
		#print(temp_size)
		if temp_sum>len(Seat):
			print("not possible")
			return 1
		Size.append(max(temp_sum,max(temp_size)))
	print(Size)

	for i in range(len(Subs)):
		z=-1
		for j in Subs[i]:
			crsr.execute('''
				select roll,sname from Subjects,Classes 
				where Subjects.class=Classes.class and Subjects.sname="{}";
				'''.format(j))
			for x,y in crsr.fetchall():
				#print(y)
				for k in range(Size[i]):
					z+=1
					if z%Size[i]==0:
						z=0
					if Seats[i][z][1]==0 and z==0:
						Seats[i][z][1]=x
						Seats[i][z][2]=y
						break
					#print(z,'-',Seats[i][z],',',Seats[i][z-1])
					if Seats[i][z][1]==0 and y!=Seats[i][z-1][2]:
						Seats[i][z][1]=x
						Seats[i][z][2]=y
						break

