class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "/", "-", "*"}
        queue = []
        for i in tokens:
            if i in operations:
                res = 0
                b, a = queue.pop(), queue.pop()
                if i == "+":
                    res = a + b
                elif i == "-":
                    res = a - b
                elif i == "/":
                    res = a / b
                else:
                    res = a * b
                queue.append(int(res))
            else:
                queue.append(int(i))
        return queue.pop()
    