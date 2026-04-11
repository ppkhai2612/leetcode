class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]": # when encounter "]", stop append to stack 
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr # take substring in []
                stack.pop() # pop "[" char

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k # take k
                stack.append(int(k) * substr)
                # stack = ["3", "[", "a", "cc"]
        
        return "".join(stack) # convert list into str and return