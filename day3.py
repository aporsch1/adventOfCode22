def main():
    with open("rucksack.txt", "r") as f:
        lines = f.readlines()
        rucksacks = [i.strip() for i in lines]
    sum=0
    while len(rucksacks)>0:
        sackOne = set(rucksacks.pop())
        sackTwo = set(rucksacks.pop())
        sackThree = set(rucksacks.pop())
        olChar= (sackOne.intersection(sackTwo)).intersection(sackThree).pop()

        if olChar.isupper()==True:
            sum+=ord(olChar)-ord("A")+27
        else:
            sum+=ord(olChar)-ord("a")+1
    print(sum)
main()



