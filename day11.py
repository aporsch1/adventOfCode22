#this is going to be so weird and I am tired and feel like I can't read or comprehend anything right now so this will be an absolute riot.
from tqdm import tqdm
class Monkey:
    def __init__(self, index: int, item_list: list[int], operation: str, division_test: int, send_list: list[int]):
        self.index = index
        self.items = item_list
        self.operation = operation
        self.test = division_test
        self.send_indices = send_list
        self.total_items_checked = 0

    def __repr__(self):
        return f"Monkey(index={self.index}, items={self.items}, operation={self.operation}, division_test={self.test}, send_indices={self.send_indices})"

    def update_items(self):
        self.items = [eval(self.operation) // 3 for old in self.items]
        self.total_items_checked+=len(self.items)

    def monkey_send(self):
        if_true_list = [item for item in self.items if item % self.test == 0]
        if_false_list = [item for item in self.items if item % self.test != 0]
        self.items = []
        return {self.send_indices[0]: if_true_list, self.send_indices[1]: if_false_list}

    def receive_items(self, items_to_receive: list[int]):
        self.items.extend(items_to_receive)

lines = open("day11.txt", "r").readlines()

def parse_monkeys(input_lines):
    indices, items, operations, division_tests, send_indices = [], [], [], [], []
    for line in lines:   
        if line.startswith('Monkey'):
            indices.append(int(line.strip()[-2]))
        elif line.strip().startswith('Starting items:'):
            items.append([int(el) for el in line.strip().replace("Starting items: ", "").split(",")])
        elif line.strip().startswith('Operation'):
            operations.append(line.strip().replace("Operation: new = ",""))
        elif line.strip().startswith('Test'):
            division_tests.append(int(line.strip().replace("Test: divisible by ", "")))
        elif line.strip().startswith('If true:'):
            current_send_indices = [int(line.strip().replace("If true: throw to monkey ", ""))]
            send_indices.append(current_send_indices)
        elif line.strip().startswith('If false:'):
            current_send_indices.append(int(line.strip().replace("If false: throw to monkey ", "")))
            send_indices.append(current_send_indices)
    return [Monkey(*args) for args in zip(indices, items, operations, division_tests, send_indices)]

monkeys = parse_monkeys(lines)

def simulate_system(monkey_list: list[Monkey]):
    for monkey in monkey_list:
        monkey.update_items()
        dict_to_send = monkey.monkey_send()
        for key in dict_to_send.keys():
            monkey_list[key].receive_items(dict_to_send[key])
    return monkey_list

def solution_one(monkey_list,nrounds):
    for _ in range(nrounds):
        monkey_list = simulate_system(monkeys)
        print(monkey_list)
    top2_monkeys = sorted([monkey.total_items_checked for monkey in monkey_list])[-2:]
    print(sorted([monkey.total_items_checked for monkey in monkey_list]))
    return top2_monkeys[0]*top2_monkeys[1]

print(solution_one(monkeys, 20))

