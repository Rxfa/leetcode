class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_number = 0
        current_string = ""

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == "[":
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0
            elif char == "]":
                last_string, repeat_count = stack.pop()
                current_string = last_string + current_string * repeat_count
            else:
                current_string += char
        return current_string
