class Solution:
    def myAtoi(self, s: str) -> int:
        signs = []
        res = ""
        for i in s:
            if i.isnumeric():
                res += i
            elif (i == "+" or i == "-") and not res:
                if signs:
                    return 0
                signs.append(i)
            elif i == " " and not res and not signs:
                continue
            else:
                break
        if not res:
            return 0
        res = int(res)
        if signs and signs[-1] == "-":
            res = -res
        if res < 0:
            res = max(-1 * math.pow(2, 31), res)
        else:
            res = min(res, math.pow(2, 31) - 1)
        return int(res)
