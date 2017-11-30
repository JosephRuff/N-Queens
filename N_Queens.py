#following allows for generation of random numbers
import random


n = 0
#the following takes an input of n
while (n<1):
    while True:
        n = raw_input("Please enter an integer: ")
        print ""
        print "You entered", n
        print ""
        try:
            n = int(n)
            break
        except ValueError:
            print "Thats not an integer."
            print ""
    if (n < 1):
        print "Number must be greater than zero." 
        print ""
        

#the following takes a state (in the n numbers format) and prints it
def printSolution(solution):
    for i in range(len(solution)):
        line = ""
        for j in range(len(solution)):
            if (solution[j] == i + 1):
                line = line + " Q "
            else:
                line = line + " - "
        print line
            

#the following takes a state (in the n numbers format) and returns true if it is a solved state
def checkIfCorrect(solution):
    #print "#"
    flag = False
    for i in range(len(solution)):
        for j in range(i+1):
            if (i != j):
                if (solution[i] == solution[j]):
                    flag = True
                if ((i - j) == abs(solution[i] - solution[j])):
                    flag = True
    if (flag == False):
        return True
    else:
        return False
    
#this checks through the entire listOfStates to see if the new state is unique
def checkIfDuplicate(listOfStates, child):
    flag = False
    for i in range (len(listOfStates)):
        if (listOfStates[i] == child):
            flag = True
    if (flag == True):
        return True
    else:
        return False
        
        
#this takes the state at the counters current location in the list and generates its children
def generateChildren(list, parent):
    for i in range(n):
        for j in range(n):
            child = parent[:]
            child[i] = j + 1
            if (checkIfDuplicate(list, child) == False):
                if (checkIfCorrect(child) == True):
                    #if child state is a solution, it is printed
                    print "Solution found: "
                    printSolution(child)
                    print ""
                #children are only appendid if they are unique
                list.append(child)
    return list


#this generates the intial state
newInitialState = []
for i in range(n):
    newInitialState.append(0)
for i in range(n):
    newNum = random.randint(1,n)
    newInitialState[i] = newNum


print "Initial state is: "
printSolution(newInitialState)
print ""

#this initialises the list
listOfStates = []
listOfStates.append(newInitialState)


#this initialises the counter
counter = 0

#this indicates that the program is actually doing something because the next step can take awhile
print "Working..."
print ""


#this is the main loop which generates all possible children for the given initial state and then through use of a counter generates all of the children for the new children
while (counter < len(listOfStates)):
    listOfStates = generateChildren(listOfStates, listOfStates[counter])
    counter = counter + 1
    

#this initialises the counters that indicate the number of solutions
noOfCorrect = 0
noOfStates = len(listOfStates)


#this goes through the newly generated list of all states and counts the number of solutions
for i in range(len(listOfStates)):
    if (checkIfCorrect(listOfStates[i])==True):
        noOfCorrect = noOfCorrect + 1
        
#this prints the number of solutions
print "There are", noOfCorrect, "solutions. "
