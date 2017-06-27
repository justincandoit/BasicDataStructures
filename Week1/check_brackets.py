# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next,i))
            pass

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) < 1:
                print(i+1)
                exit()
            top = opening_brackets_stack.pop()
            if top.Match(next):
                pass
            else:
                print(i + 1)
                exit()




    # Printing answer, write your code here
    if opening_brackets_stack:
        top = opening_brackets_stack.pop()
        print(top.position+1)
    else:
        print('Success')
