class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Невозможно извлечь элемент из пустого стека")

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print("Элементы стека:", self.items)

stack = Stack()
stack.push(15)
stack.push(25)
stack.push(35)
stack.push(45)
stack.push(55)

stack.display()

popped_item = stack.pop()
print("Извлеченный элемент:", popped_item)

popped_item = stack.pop()
print("Извлеченный элемент:", popped_item)

stack.display()
