#this is going to be so weird and I am tired and feel like I can't read or comprehend anything right now so this will be an absolute riot.

class monkey:
    def __init__(self, index: int, item_list: list[int], operation: str, division_test: int, send_list: list[int]):
        self.index = index
        self.items = item_list
        self.operation = operation
        self.test = division_test
        self.send_indices = send_list
        self.total_items_checked = 0

    def __repr__(self):
        return f"Monkey(index={self.index}, items={self.items}, operation={self.operation}, division_test={self.division_test}, send_indices={self.send_indices})"

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

