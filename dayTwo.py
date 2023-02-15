resultMap={'A':'Rock','B':'Paper','C':'Scissors','X':'Loss','Y':'Draw','Z':'Win'}
pointsPerThrow={'Rock':1,'Paper':2,'Scissors':3}
wld={'Win':6,'Draw':3,'Loss':0}


def main():
    with open("RPS.txt","r") as f:
        lines=f.readlines()
        games = [entry.strip() for entry in lines]
    pointSum=sum([ppr(round)for round in games])
    print(pointSum)

def ppr(round):
    oppThrow=resultMap[round[0]]
    myGoal=resultMap[round[2]]
    if (oppThrow, myGoal) in [('Rock', 'Draw'), ('Paper', 'Loss'), ('Scissors', 'Win')]:
        return (wld[myGoal]+pointsPerThrow['Rock'])
    elif (oppThrow, myGoal) in [('Paper', 'Draw'), ('Rock', 'Win'), ('Scissors', 'Loss')]:
        return (wld[myGoal]+pointsPerThrow['Paper'])
    else:
        return (wld[myGoal]+pointsPerThrow['Scissors'])

main()


