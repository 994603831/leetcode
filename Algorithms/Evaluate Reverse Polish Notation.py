class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in range(0,len(tokens)):
            if tokens[i] != '+' and tokens[i] != '-' and tokens[i] != '*' and tokens[i] != '/':
                stack.append(int(tokens[i]))
            else:
                a = stack.pop()
                b = stack.pop()
                if tokens[i] == '+':
                    stack.append(a+b)
                if tokens[i] == '-':
                    stack.append(b-a)
                if tokens[i] == '*':
                    stack.append(a*b)
                if tokens[i] == '/':
                    if a*b < 0:
                        stack.append(-((-b)/a))
                    else:
                        stack.append(b/a)
        return stack.pop()