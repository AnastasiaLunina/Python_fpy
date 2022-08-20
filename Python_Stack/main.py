"""
A stack is a linear data structure that stores items in a Last-In/First-Out (LIFO) or First-In/Last-Out (FILO) manner.
In stack, a new element is added at one end and an element is removed from that end only.
1. Create class Stack  with following methods:
isEmpty(), push(), pop(), peek(), size()
2. Using this class write a function to check if set of brackets are balanced correctly.
For each opening bracket there is corresponding closing bracket.
"""


class Stack:

    def __init__(self):
        self.stack_list = []

    def is_empty(self):
        """
        checks if stack is empty
        :return: Boolean
        """
        return len(self.stack_list) == 0

    def push(self, item):
        """
        adds new item on top of the stack
        :param item:
        :return: nothing
        """
        self.stack_list.append(item)

    def pop(self):
        """
        deletes topmost element of the stack
        :return: top element of the stack
        """
        if not self.is_empty():
            return self.stack_list.pop()

    def peek(self):
        """
        stack stays the same
        :return: top element of the stack
        """
        if not self.is_empty():
            return self.stack_list[-1]

    def size(self):
        """
        checks the stack length
        :return: stack length
        """
        return len(self.stack_list)


def check_balanced_brackets(sequence):
    """
    Using the class Stack checks if given sequence of brackets is balanced correctly
    :param sequence:
    :return: Boolean
    """
    stack = Stack()
    bracket_dict = {
            '(': ')',
            '[': ']',
            '{': '}'
    }
    for bracket in sequence:
        if bracket in bracket_dict:
            stack.push(bracket)
        elif bracket == bracket_dict.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':
    test = ['(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for pattern in test:
        if check_balanced_brackets(pattern):
            print(f'{pattern:<30} Balanced')
        else:
            print(f'{pattern:<30} Not Balanced')


