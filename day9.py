import numpy as np
#code starts here
with open("day9.txt", "r") as file:
    lines = file.readlines()
    movements = [(i.strip().split(' ')[0], int(i.strip().split(' ')[1])
     )
     for i in lines]
    
def update_tail(head, tail):
    difference = head - tail
    req_change = {
        (2, 1):(1, 1),
        (1, 2):(1, 1),
        (2, 0):(1, 0),
        (2, -1):(1, -1),
        (1, -2):(1, -1),
        (0, -2):(0, -1),
        (-1, -2):(-1,-1),
        (-2, -1):(-1, -1),
        (-2, 0):(-1, 0),
        (-2, 1):(-1, 1),
        (-1, 2):(-1, 1),
        (0, 2):(0, 1),
        (2, 2):(1, 1),
        (-2, -2):(-1, -1),
        (-2, 2):(-1, 1),
        (2, -2):(1, -1)
    }
    new_tail_position = tail + np.array(req_change.get(tuple(difference), (0,0)))
    return new_tail_position
def update_head(head, direction):
    if direction == 'R':
        head[1] += 1
    elif direction == 'L':
        head[1] -= 1
    elif direction == 'U':
        head[0] += 1
    elif direction == 'D':
        head[0] -= 1
    return head
def main():
    head = np.array([0,0])
    tail = np.array([0,0])
    tail_positions = set([tuple(tail)])
    for direction, distance in movements:
        while distance > 0:
            head = update_head(head, direction)
            distance -= 1
            tail = update_tail(head, tail)
            tail_positions.add(tuple(tail))
    print("part one solution: ")
    print(len(tail_positions))
        #print(f"{head=}, {tail=}")
    rope = [np.array([0,0]) for _ in range(10)]

    tail_positions = set([tuple(rope[9])])
    for direction, distance in movements:
        while distance > 0:
            rope[0] = update_head(rope[0], direction)
            distance -= 1
            for i in range(1, len(rope)):
                rope[i] = update_tail(rope[i-1], rope[i])
            tail_positions.add(tuple(rope[9]))
    
    print("part two solution: ")
    print(len(tail_positions))
main()
