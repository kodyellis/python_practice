#!/usr/bin/python3
limitX = 10
limitnegX = -10
limitY = 20
limitnegY = -20

rooms = ['North room', 'South room','East Room', 'West Room']
def userCtl(steps):
    #The user use the function to control movement


    if moveXR == limitX:
        rply = "Entering %s" % rooms[2]

    elif moveXL == limitnegX:
        rply = "Entering %s" % rooms[3]

    elif moveYF == limitY:
        rply = "Entering %s" % rooms[0]
    elif moveYB == limitnegY:
        rply = "Entering %s" % rooms[1]

print("Enter movement numbers")
