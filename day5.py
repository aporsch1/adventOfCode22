
def main():
    f1 = open("crates.txt", "r")
    f2 = open("crates.txt", "r")
    partOne(f1)
    partTwo(f2)
def separateFile(file):
    levels, instructions = [section.split("\n") for section in file.read().split("\n\n")]
    levels = [crate.replace("    ", " [X] ") for crate in levels[:-1]]
    levels = [[crate[1] for crate in level.split()] for level in levels]
    stacks = [[] for i in range(len(levels[0]))]
    for level in reversed(levels):
        for index, crate, in enumerate(level):
            if crate != "X":
                stacks[index].append(crate)
    return instructions, levels, stacks
def partOne(file):
    instructions, levels, stacks = separateFile(file)
    for inst in instructions:
        num, fromOrder, toOrder = [int(i) for i in inst.split(" ") if i.isnumeric()]
        while num != 0:
            stacks[toOrder-1].append(stacks[fromOrder-1].pop())
            num-=1
    [print(stack[-1], end="") for stack in stacks]
def partTwo(file):
    instructions, levels, stacks = separateFile(file)
    for instruction in instructions:
        num, fromOrder, toOrder = [int(i) for i in instruction.split(" ") if i.isnumeric()]
        fromStack = stacks[fromOrder-1]
        stacks[toOrder-1].extend(fromStack[len(fromStack)-num:])  # Move crates all at once
        stacks[fromOrder-1] = fromStack[:len(fromStack)-num]
    print()
    [print(stack[-1], end="") for stack in stacks]
main()




