class Stack:
    def __init__(self, definition):
        self.stack = list(definition)

    def add(self, items):

        for i in items:
            self.stack.append(i)

    def top(self):
        return str(self.stack[len(self.stack)-1])

    def move(self, itemCount):
        movedItems = list()

        itemCounter = 0

        while itemCounter != itemCount:
            movedItems.append(self.stack.pop())
            itemCounter += 1

        movedItems.reverse()
        
        return movedItems


class Stacks:
    def __init__(self, definition):
        self.stacks = list()

        for s in definition:
            self.stacks.append(s)
    
    # "move 1 from 1 to 2"
    def action(self, commandText):
        command = Command(commandText)
        movedItems = self.stacks[command.fromStack].move(command.moveItems)

        self.stacks[command.toStack].add(movedItems)

    def top(self):
        topItems = list()
        
        for s in self.stacks :
            topItems.append(s.top())

        return "".join(topItems)

class Command:
    def __init__(self, definition):
        components = definition.split()

        self.moveItems = int(components[1])
        self.fromStack = int(components[3]) - 1
        self.toStack = int(components[5]) - 1

