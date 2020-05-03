import manualinit2 as man
import autoinit2 as auto
from projectsupport import *
import sqlite3
import os

os.remove("Database.db")

Section={}
Subject={}
allocated_sec={}
Seat=[]
#print(Seat)
Subjects={}
Day_arrangement={}
Ndays=0
Seats=[]



def main():
    db=sqlite3.connect("Database.db")
    cursor=db.cursor()
    #print('Would you like : \n1. Results with predefined constraints\n2. Manual inputs')
    #choice=int(input('Please select : '))
    choice=2								#currently set to auto
    if choice==1:
        op=auto
    elif choice==2:
        op=man
    else:
        print("Wrong choice")
    op.section_creator(cursor)
    #print(Section)
    op.subject_allocator(Seat,cursor)
    assign_days(Day_arrangement,cursor)
    #print(Subjects)
    arrangement(Seat,Seats,Day_arrangement)

    #for i in Seats:
    #	print(i)

    for i in Seats:
	    print('\n-------------\n')
	    for x,y,z in i:
	    	if (x-1)%6==0:
	    		print()
	    	if(y==0):
	    		print('     |  ',end='\t')
	    	else:
	    		print(y,'|',z,end='\t')
    print()
    #print(Subjects)

main()
