file  = open("day10.txt", "r")
lines =  file.read().strip().splitlines()

def main():
    X = 1
    cycle = 1
    accum = 0
    for i in lines:
        cycle+=1
        if cycle % 40 == 20:
            accum = accum + X
        if i.startswith('addx '):
            if cycle % 40 == 20:
                accum = accum + X
            cycle = cycle + 1
            if cycle % 40 == 20:
                accum = accum + X
           #print(int(i[5:]))
            X=X+int(i[5:])
        if cycle % 40 == 20:
            accum = accum + 1
        print(accum)
    print(cycle)
    print(accum)
    
main()


