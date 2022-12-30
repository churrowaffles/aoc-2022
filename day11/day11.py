import operator
import re

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

class Monkey:
    def __init__(self, index):
        self.index = index
        self.items = []
        self.inspection = 0
        
    def set_operation(self, operator, value):
        if not operator or not value:
            return False
        self.operator = operator
        self.value = value

    def worry_level(self):
        if self.value == "old":
            return ops[self.operator](int(self.items[0]), int(self.items[0]))
        return ops[self.operator](int(self.items[0]), int(self.value))

    def set_test(self, divisor, truth_monkey, false_monkey):
        self.divisor = int(divisor)
        self.truth_monkey = int(truth_monkey)
        self.false_monkey = int(false_monkey)
    
    def to_receive(self, worry_level):
        if worry_level % self.divisor:
            return self.false_monkey
        return self.truth_monkey

all_monkeys = []

with open("day11.txt", "r") as file:
    for line in file:
        if line.startswith("Monkey"):
            monkey_index = int(line.split()[1][:-1])
            all_monkeys.append(Monkey(monkey_index))
        elif "Starting" in line:
            all_monkeys[-1].items += re.findall(r'\d+', line)
        elif "Operation" in line:
            operator, value = line.replace("Operation: new = old", "").lstrip().split()
            all_monkeys[-1].set_operation(operator, value)
        elif "Test" in line:
            divisor = line.split()[-1]
            truth_monkey = next(file).split()[-1]
            false_monkey = next(file).split()[-1]
            all_monkeys[-1].set_test(divisor, truth_monkey, false_monkey)

# PART ONE SOLUTION
for rounds in range(20):
    for monkey in all_monkeys:
        while len(monkey.items) > 0:
            new_worry_level = monkey.worry_level() // 3
            monkey_to_receive = monkey.to_receive(new_worry_level)
            monkey.items.pop(0)
            all_monkeys[monkey_to_receive].items.append(new_worry_level)
            monkey.inspection += 1

monkey_business = [monkey.inspection for monkey in all_monkeys]
monkey_business.sort(reverse=True)
print("Monkey Business is", monkey_business[0] * monkey_business[1])
