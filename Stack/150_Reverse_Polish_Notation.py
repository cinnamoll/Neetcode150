class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if (i == "+"):
                st.append(st.pop() + st.pop())
            elif (i == '-'):
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif (i == '*'):
                st.append(st.pop() * st.pop())
            elif (i == '/'):
                second, first = st.pop(), st.pop()
                st.append(int(first/second))
            else:
                st.append(int(i))
        return st[0]