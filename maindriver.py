import manualinit as man
import autoinitializer as auto

Section={}
Subject={}
Seat=[]
#print(Seat)
Subjects={}


def sortedSubjects():
    #print(Subject)
    Sub=dict(Subject)
    #print(len(Sub))
    for k in range(len(Sub)):
        max=-1000
        maxi=''
        #print(len(Sub))
        for i in Sub:
            #print(len(Sub[i]))
            #print(max,' ',len(Sub[i]))
            if max<len(Sub[i]):
                max=len(Sub[i])
                maxi=i
        #print('max at ',k,' =',maxi,' ',max)
        Subjects[maxi]=Sub[maxi]
        Sub.pop(maxi)
 

def arrangement():
    #print(Subjects)
    count=0
    for i in Subjects:
        #print('inside Subjects')
        #print(len(Subjects[i]),' ',(len(Seat)+1)/2)
        count+=len(Subjects[i])
        if len(Subjects[i])>((len(Seat)+1)/2) or count>len(Seat):
            print("Not possible")
            if count>len(Seat):
                print('Less seats available')
            else:
                print('Arrangment without same Subject not sitting next to each other not possible')
            return;
    print('Possible')
    for i in Subjects:
        for j in Subjects[i]:
            #print(j)
            for z in range(len(Seat)):
                if z!=0:
                    #print('Inside',z)
                    pev=Seat[z-1][1]
                    if pev in Subjects[i]:
                        continue
                    #print(Seat[z],' ',pev)
                #print('regular')
                if Seat[z][1]==0:
                    #print('Not empty')
                    Seat[z][1]=j
                    Seat[z][2]=i
                    break;
                    

def main():
    print('Would you like : \n1. Results with predefined constraints\n2. Manual inputs')
    choice=int(input('Please select'))
    if choice==1:
        op=auto
    elif choice==2:
        op=man
    else:
        print("Wrong choice")
    op.section_creator(Section)
    #print(Section)
    op.subject_allocator(Subject,Seat)
    print('-------------')
    sortedSubjects()
    #print(Subjects)
    arrangement()
    print(Seat)


main()
