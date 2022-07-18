class Solution:
    def interpret(self, command: str) -> str:
        s, i = '', 0
        while i < len(command):
            if command[i] == '(' and command[i+1] == ')':
                s += 'o'
                i += 2
            elif command[i] == 'G':
                s += 'G'
                i += 1
            else:
                s += 'al'
                i += 4
        return s