class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Peek into an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

if __name__ == "__main__":
    # example
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(stack.pop())  # Output: 3
    print(stack.peek())  # Output: 2
    print(stack.size())  # Output: 2
