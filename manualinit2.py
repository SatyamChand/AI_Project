def section_creator(cursor):    #to create and assign registration numbers to students
    s=int(input("Enter the size of one section : "))    #currently fixed sized classes
    n=int(input("Enter the no. of sections : "))
    
    roll=[]
    for i in range(n):
        name="Class"+str(i+1)
        roll.extend(list((i,name)for i in range(1001+i*s,1001+(i+1)*s)))
    #print(roll)
    cursor.execute('''
        create table Classes(
        roll int,
        class varchar(5)
        );
        ''')
    #print(rolls)
    cursor.executemany('''
        insert into Classes values (?,?);
        ''',roll)


def subject_allocator(Seat,cursor):
    choice='y'
    subjects=[]

    cursor.execute('''select class from Classes group by class;''')
    classes=cursor.fetchall()
    classes=list(i[0] for i in classes)
    
    cursor.execute('''create table Subjects(
        sname varchar(30),
        class varchar(5)
        );''')

    while choice=='y':              #to ue change to y
        name=input("\nEnter the subject name : ")
        sections=input("Enter the section names(separated only by a ',') : ")
        choice=input("\nDo you want to enter more classes (y/n) : ")
        sections=sections.split(',')
        for i in sections:
            if i not in classes:
                print(classes)
                print('\n',i,' is not a valid section')
            else:
                subjects.append((name,i))
    #print(subjects)
    cursor.executemany('''insert into Subjects values(?,?);''',subjects)

    seat_creator(Seat)

def seat_creator(Seat):
    seat=int(input("\nEnter the no. of seats available : "))
    for i in range(1,seat+1):
        Seat.append([i,0,''])




