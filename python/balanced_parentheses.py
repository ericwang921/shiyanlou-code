# -*- coding: UTF-8 -*-

from data_structure.stack import Stack

def balanced_parentheses(parentheses):
    stack = Stack(len(parentheses))
    for str in parentheses:
        if str == '(':
            stack.push(str)
        elif str == ")":
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()


if __name__ == '__main__':
    examples = ['((()))', '((())', '(()))', '(()()((())))', '(())()()']
    print('Balanced parentheses demonstration:\n')
    for example in examples:
        print(example + ': ' + str(balanced_parentheses(example)))
