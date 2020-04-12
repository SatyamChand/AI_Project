def section_creator(Section):    #to create and assign registration numbers to students
    s=2                 #currently fixed
    n=5                 #for testing
    
    for i in range(n):
        name="Class"+str(i+1)
        roll=list(range(1001+i*s,1001+(i+1)*s))
        #print(name,' ',roll)
        Section[name]=roll
        
def subject_allocator(Section,Subject,allocated_sec,Seat):
    Subject['Python']=[1001,1002,1003,1004]
    Subject['DBMS']=[1005,1006,1007,1008,1009,1010]
    Subject['AI']=[1011,1012,1013,1014,1015]
    Subject['C']=[1016,1017,1018,1019,1020,1021,1022,1023,1024,1025]
    #print(Subject)
    for i in range(1,36):
        Seat.append([i,0,''])

