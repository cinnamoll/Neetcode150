class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = []

        for p, s in sorted(pair)[::-1]:
            temp = (target - p) / s
            stack.append(temp)
            if len(stack) > 1 and temp <= stack[-2]:
                stack.pop()
        return len(stack)