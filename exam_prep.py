# # l = [40, 269, 167, 299, 140]
# # for i in l:
# #     print(i//10z%10)
# # def find(*args):
# #     gcd = 0
# #
# #     for i in range(1, min(*args)+1):
# #         if all([True if x % i == 0 else False for x in nums ]):
# #             gcd = i
# #
# #
# #     return gcd
# #
# #
# #
# # nums = [6, 12, 36, 6]
# # print(find(*nums))
# #
# # class Person:
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def output(self):
# #         return f'{self.name}, {self.age}'
# #     def __str__(self):
# #         return self.output()
# #
# #     def __repr__(self):
# #         return self.output()
# #
# # ayugdu = Person('hoho', 4)
# # print(ayugdu)
# import math
#
# from typing import Union
#
#
# def remove_brackets(line: str) -> str:
#     # your code here
#     stack = []
#     result = list(line)
#
#     for i, char in enumerate(line):
#         if char in "({[":
#             stack.append((char, i))
#         elif char in ")}]":
#             if stack and is_matching(stack[-1][0], char):
#                 stack.pop()
#             else:
#                 result[i] = ''
#
#     # Remove brackets marked for removal
#     result = ''.join(result)
#
#     return result
#
#
# def is_matching(opening, closing):
#     return (opening == '(' and closing == ')') or \
#         (opening == '[' and closing == ']') or \
#         (opening == '{' and closing == '}')
#
#
#
#
#
# print("Example:")
# print(remove_brackets("(()()"))
#
# # These "asserts" are used for self-checking
# assert remove_brackets("(()()") == "()()"
# assert remove_brackets("[][[[") == "[]"
# assert remove_brackets("[[(}]]") == "[[]]"
# assert remove_brackets("[[{}()]]") == "[[{}()]]"
# assert remove_brackets("[[[[[[") == ""
# assert remove_brackets("[[[[}") == ""
# assert remove_brackets("") == ""
# assert remove_brackets("[(])") == "()"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
#
#
def remove_brackets(expression):
    stack = []
    result = list(expression)

    for i, char in enumerate(expression):
        if char in "({[":
            stack.append((char, i))
        elif char in ")}]":
            for idx in range(-1, -len(stack) - 1, -1):
                if stack and is_matching(stack[idx][0], char):
                    stack.pop(idx)
                    break

            else:
                result[i] = ''

    # Remove unmatched opening brackets
    for opening, i in stack:
        result[i] = ''

    # Remove brackets marked for removal
    result = ''.join(result)

    return result


def is_matching(opening, closing):
    return (opening == '(' and closing == ')') or \
        (opening == '[' and closing == ']') or \
        (opening == '{' and closing == '}')


# Test cases
assert remove_brackets("(()()") == "()()"
assert remove_brackets("[][[[") == "[]"
assert remove_brackets("[[(}]]") == "[[]]"
assert remove_brackets("[[{}()]]") == "[[{}()]]"
assert remove_brackets('[(])') == '()'
print("All test cases passed!")
