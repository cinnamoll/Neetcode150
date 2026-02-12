class Solution:
    def isValid(self, s: str) -> bool:
        check = []
        for c in s:
            if len(check) == 0:
                check.append(c)
            elif (c == ')' and check[-1] == '(') or (c == ']' and check[-1] == '[') or (c == '}' and check[-1] == '{'):
                check.pop()
            else:
                check.append(c)
        return len(check) == 0