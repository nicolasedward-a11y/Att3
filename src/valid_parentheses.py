from src.my_stack import MyStack


def is_valid_parentheses(string: str) -> bool:
    stack = MyStack()

    pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in string:
        if char in '([{':
            stack.push(char)

        elif char in ')]}':
            top = stack.pop()

            if top != pairs[char]:
                return False

    return stack.is_empty()
