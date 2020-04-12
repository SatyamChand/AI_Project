def section_creator(Section):    #to create and assign registration numbers to students
    s=int(input("Enter the size of one section : "))    #currently fixed sized classes
    n=int(input("Enter the no. of sections : "))
    
    for i in range(n):
        name="Class"+str(i+1)
        roll=list(range(1001+i*s,1001+(i+1)*s))
        print(name,' ',roll)
        Section[name]=roll


def subject_allocator(Section,Subject,allocated_sec,Seat):
    choice='y'
    while choice=='y':              #to ue change to y
        name=input("\nEnter the subject name : ")
        sections=input("Enter the section names(separated only by a ',') : ")
        choice=input("\nDo you want to enter more classes (y/n) : ")
        allocated_sec[name]=sections.split(',')
        for i in allocated_sec:
            for j in allocated_sec[i]:
                if j not in Section:
                    print('\n',j,' is not a valid section')
                    allocated_sec[i].remove(j)
    for i in allocated_sec:
        Subject[i]=[]
        for j in allocated_sec[i]:
            #print(i,' ',Section[j])
            for k in Section[j]:
                Subject[i].append(k)
    seat_creator(Seat)

def seat_creator(Seat):
    seat=int(input("\nEnter the no. of seats available : "))
    for i in range(1,seat+1):
        Seat.append([i,0,''])




