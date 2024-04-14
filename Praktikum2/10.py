class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Невозможно извлечь элемент из пустой очереди")

    def is_empty(self):
        return len(self.items) == 0

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print("Текущая очередь:", queue.items)

dequeued_item = queue.dequeue()
print("Извлеченный элемент:", dequeued_item)

dequeued_item = queue.dequeue()
print("Извлеченный элемент:", dequeued_item)

print("Обновленная очередь:", queue.items)
