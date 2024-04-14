class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Не удается извлечь из пустой стопки"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Пустая стопка"

stack = Stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Размер стека:", stack.size())
print("Первый элемент:", stack.peek())

popped_item = stack.pop()
print("\nИзвлеченный элемент:", popped_item)

print("\nРазмер стека:", stack.size())
print("Верхний элемент:", stack.peek())
