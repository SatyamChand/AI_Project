def section_creator(cursor):    #to create and assign registration numbers to students
    s=5                 #currently fixed
    n=4                 #for testing
    
    rolls=[]
    
    for i in range(n):
        name="Class"+str(i+1)
        roll=list(range(1001+i*s,1001+(i+1)*s))
        #print(name,' ',roll)
        Section={}
        Section[name]=roll
        for i in Section[name]:
            rolls.append((i,name))
    cursor.execute('''
        create table Classes(
        roll int,
        class varchar(5)
        );
        ''')
    #print(rolls)
    cursor.executemany('''
        insert into Classes values (?,?);
        ''',rolls)
    # cursor.execute("select * from Class1;")
    # data=cursor.fetchall()
    # for i in data:
    #     print(i)

        
def subject_allocator(Seat,cursor):
    #print(Section)
    allocated_sec={}
    allocated_sec['AI']=['Class1','Class3']
    allocated_sec['C']=['Class2','Class3','Class4']
    allocated_sec['DB']=['Class4']

    cursor.execute('''create table Subjects(
        sname varchar(30),
        class varchar(10)
        );
        ''')

    for i in allocated_sec:
        for j in allocated_sec[i]:
            cursor.execute('''insert into Subjects(sname,class) values('{}','{}')'''.format(i,j))

    print("subjects allocated")
    #print(allocated_sec)
    #print(Subject)
    for i in range(1,37):
        Seat.append([i,0,''])
