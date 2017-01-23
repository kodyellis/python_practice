import os
import sys
#-------------------------------->
''' The functions below perform Write, Read, Rename, Append, and Remove
operations on files'''
def writF(choice):
    print("Write what you want in the file")
    words=input()
    myfile=open(choice,"w")
    myfile.write(words)
    print("Here what you wrote: %s" % words)
    input("Press enter to return to menu")
    myfile.close()
    #---------------------------------------->
def add(choice):
    print("Write what you want append to the file")
    words=input()
    myfile=open(choice,"a")
    myfile.write(words)
    print("Here what you add: %s" % words)
    input("Press enter to return to menu")
    myfile.close()
    #---------------------------------------->
def readF(choice):
    myfile=open(choice,"r")
    readIT=myfile.read()
    print(readIT)
    input("Press enter to return to menu")
    myfile.close()
    #---------------------------------------->
def renamer(choice):
    print("Rename your file below")
    nameNew=input()
    print(" %s has been change to %s" % (choice,nameNew))
    input("Press enter to return to menu")
    os.rename(choice,nameNew)
    #---------------------------------------->
def remove(choice):
    print("The file: %s will be delete. Remove the file?(Y/N)" % choice)
    answer=input()
    if(answer == "Y"):
        os.remove(choice)
        print(" %s is deleted" % choice)
    if(answer == "N"):
        print(" %s not removed" % choice)
    input("Press enter to return to menu")
    #---------------------------------------->
def print_menu():       ## Your menu design here
    print (10 * "<-" , "MENU" , 10 * "->")
    print ("Write to a file:(type W)")
    print ("Print the Contents of file:(type P)")
    print ("Add text to a file:(type A)")
    print ("Rename a file:(type R)")
    print ("Delete a file:(type D)")
    print ("Exit Menu:(type E)")
    print (20 * "<->")
#----------------------->

loop=True
while loop:
    print("Select a file operation")
    print_menu()
    options=input()
    if(options == "E"):
        sys.exit()
    else:
        print("Choose a file")
        choice=input()
        if(options == "W"):
            writF(choice)
        elif(options == "A"):
            add(choice)
        elif(options == "P"):
            readF(choice)
        elif(options == "R"):
            renamer(choice)
        elif(options == "D"):
            remove(choice)
