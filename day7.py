from collections import defaultdict

with open("day7.txt", "r") as f:
    commands = f.readlines()

weights=defaultdict(int)
stack = []

for command in commands:
    if command.startswith("$ ls") or command.startswith("dir"):
        continue
    if command.startswith("$ cd"):
        x = command.split()[2]
        if x == "..":
            stack.pop()
        else:
            path = f"{stack[-1]}_{x}" if stack else x
            stack.append(path)
    else:
        size, item = command.split()
        for path in stack:
            weights[path]+=int(size)
minSize=30000000-(70000000-weights["/"])#sorting for part 2
for weight in sorted(weights.values()):
    if weight > minSize:
        break
print(sum(n for n in weights.values() if n<= 100000))#part1
print(weight)#part2
