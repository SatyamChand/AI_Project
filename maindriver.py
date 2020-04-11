import manualinit as man
import autoinitializer as auto
from projectsupport import *

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
 
def check_possible_arrangement():
    Day_arrangement=[[len(Seat),0,0]]
    print(len(allocated_sec))
    print(allocated_sec)
    for i in allocated_sec:
        print(i)
        count=0
        for j in allocated_sec[i]:
            count+=len(Section[j])
        print(count)

        for j in allocated_sec[i]:
            print('\t',j)
            for k in allocated_sec:
                print('\t\t',k)
                if i!=k  and j in allocated_sec[k]:
                    flag=1
                    print(i,' != ',k,' and ',j ,' in ',allocated_sec[k])
                    for l in range(len(Day_arrangement)):
                        if Day_arrangement[l][0]+count<=len(Seat) and i not in Day_arrangement[l]:
                            print('\t\t',k,' not in ', l)
                            Day_arrangement[l].append(i)
                            Day_arrangement[l][0]+=count
                            print('Added on day ',l)
                            flag=0
                            break
                    if flag:
                        Day_arrangement.append([count,i])
                        print('Added new day')
                        
    print(Day_arrangement)

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
