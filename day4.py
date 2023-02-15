def main():
    with open("sections.txt", "r") as f:
        lines = f.readlines()
        pairAssignments = [i.strip() for i in lines]
    overlaps=0
    for i in pairAssignments:
        assignments = i.split(",")
        rangeOne=assignments[0]
        rangeTwo = assignments[1]
        starts_ends_one=rangeOne.split("-")
        starts_ends_two=rangeTwo.split("-")
        startOne=int(starts_ends_one[0])
        #print(startOne)
        endOne=int(starts_ends_one[1])
        #print(endOne)
        startTwo=int(starts_ends_two[0])
        #print(startTwo)
        endTwo=int(starts_ends_two[1])
        #print(endTwo)
        if((endOne>=startTwo and endOne<=endTwo) or (startTwo<=endOne and endTwo>=startOne)):
            overlaps+=1
    print(overlaps)
main()

    
