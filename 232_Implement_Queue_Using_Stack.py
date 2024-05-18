class MyQueue:

    def __init__(self):
        self.addedElems = []
        self.removedElems = []

    def push(self, x: int) -> None:
        self.addedElems.append(x)

    def pop(self) -> int:
        elem = self.peek()
        self.removedElems.append(elem)
        return elem
        

    def peek(self) -> int:
        return self.addedElems[len(self.removedElems)]

    def empty(self) -> bool:
        return len(self.addedElems) == len(self.removedElems)    

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
