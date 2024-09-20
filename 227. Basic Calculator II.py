class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operations = {"+", "*", "-", "/"}
        num = ""
        ans = 0
        idx = 0
        while idx < len(s):
            while idx < len(s) and s[idx].isdigit():
                num += s[idx]
                idx += 1
            else:
                if num:
                    if stack and stack[-1] == "*":
                        stack.pop()
                        stack[-1] *= int(num)
                    elif stack and stack[-1] == "/":
                        stack.pop()
                        stack[-1] = stack[-1] // int(num)
                    else:
                        stack.append(int(num))
                num = ""
            if idx < len(s) and s[idx] in operations:
                stack.append(s[idx])
            idx += 1

        while len(stack) > 1:
            num = stack.pop()
            op = stack.pop()
            if op == "+":
                ans += num
            else:
                ans -= num
        if stack:
            return ans + stack[-1]
        return ans
            