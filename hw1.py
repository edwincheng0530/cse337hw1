from collections import Counter
import os
# PROBLEM 1
def isValid(string):
    charFrequency = {}
    for character in string:
        if character in charFrequency:
            charFrequency[character] += 1
        else:
            charFrequency[character] = 1

    charFrequency = Counter(string)

    lengthFrequency = {}
    for frequency in charFrequency.values():
        if frequency in lengthFrequency:
            lengthFrequency[frequency] += 1
        else:
            lengthFrequency[frequency] = 1

    keys = list(lengthFrequency.keys())
    if len(keys) == 1:
        return 'YES'
    if len(keys) > 2:
        return 'NO'

    diff1 = abs(keys[0]-keys[1])*abs(lengthFrequency[keys[0]])
    diff2 = abs(keys[0]-keys[1])*abs(lengthFrequency[keys[1]])

    if diff1 <= 1 or diff2 <= 1:
        return 'YES'
    else:
        return 'NO'

print("Problem 1:")
# Given Test Cases
print(isValid('aabbcd'))
print(isValid('aabbbcdddeefghi'))
print(isValid('abcdefghhgfedecba'))
# My Test Cases
print('\n' + isValid('a'))                       # YES
print(isValid('aaaaa'))                          # YES
print(isValid('abababa'))                        # YES
print(isValid('aaabbbcccdddeef'))                # NO
print(isValid('abcdefghijklmnopqrstuvwxyzz'))    # YES
print(isValid('aabcdefghijklmnopqrstuvwxyzz'))   # NO

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PROBLEM 2
def isBalanced(string):
    stack = []
    open = {'{', '[', '('}
    close = {'}', ']', ')'}
    dict = {'}': '{', ']': '[', ')': '('}

    for bracket in string:
        if bracket in open:
            stack.append(bracket)
        elif bracket in close:
            if stack:
                poppedBracket = stack.pop()
            else:
                return 'NO'
            if poppedBracket != dict[bracket]:
                return 'NO'

    if len(stack) > 0:
        return 'NO'

    return 'YES'

print("\nProblem 2:")
# Given Test Cases
print(isBalanced('{[()]}'))
print(isBalanced('{[(])}'))
print(isBalanced('{{[[(())]]}}'))
print(isBalanced('[{}]()'))
print(isBalanced('[{}()]'))
print(isBalanced('[{}]()'))

# My Test Cases
print('\n' + isBalanced('}{'))      # NO
print(isBalanced('{({})}]'))        # NO
print(isBalanced('([][])('))        # NO
print(isBalanced('({}[)]'))         # NO
print(isBalanced('{{([][])}[()]}')) # YES
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PROBLEM 3
class Node:
    def __init__(self, label, leftChild = None, rightChild = None):
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.label = label

    def recursive(self, node, list, order):
        if(node is None):
            return

        if order == 1:
            list.append(node.label)
        self.recursive(node.leftChild, list, order)
        if order == 2:
            list.append(node.label)
        self.recursive(node.rightChild, list, order)
        if order == 3:
            list.append(node.label)
        return list

    def preOrder(self):
        list = []
        self.recursive(self, list, 1)
        return list


    def inOrder(self):
        list = []
        self.recursive(self, list, 2)
        return list

    def postOrder(self):
        list = []
        self.recursive(self, list, 3)
        return list

    def sumTree(self):
        def sum(node):
            if node is None:
                return 0

            # Sum the current node's value and the sums of the left and right children
            total = int(node.label)
            total += sum(node.leftChild)
            total += sum(node.rightChild)

            return total

        return sum(self)


print("\nProblem 3:")
# Given Test Cases
root = Node(2, Node(1, Node(6), Node(3)), Node(3, None, Node(9)))
print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.sumTree())

root = Node(1, Node(2, Node(3)), Node(4, None, (Node(5, None, Node(6, None, Node(7))))))
print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.sumTree())

#My Test Cases
root = Node(1,
            Node(2),
            Node(3))
assert root.preOrder() == [1, 2, 3]
assert root.inOrder() == [2, 1, 3]
assert root.postOrder() == [2, 3, 1]
assert root.sumTree() == 6
print()
print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.sumTree())

root = Node(7)
assert root.preOrder() == [7]
assert root.inOrder() == [7]
assert root.postOrder() == [7]
assert root.sumTree() == 7
print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.sumTree())

root = Node(5,
            Node(4, Node(3)))
assert root.preOrder() == [5, 4, 3]
assert root.inOrder() == [3, 4, 5]
assert root.postOrder() == [3, 4, 5]
assert root.sumTree() == 12
print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.sumTree())


root = Node(-1,
            None,
            Node(-2, None, Node(-3)))
assert root.preOrder() == [-1, -2, -3]
assert root.inOrder() == [-1, -2, -3]
assert root.postOrder() == [-3, -2, -1]
assert root.sumTree() == -6
print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.sumTree())

root = Node(10,
            Node(5,
                 Node(1), Node(7)),
            Node(15,
                 Node(12), Node(20)))

assert root.preOrder() == [10, 5, 1, 7, 15, 12, 20]
assert root.inOrder() == [1, 5, 7, 10, 12, 15, 20]
assert root.postOrder() == [1, 7, 5, 12, 20, 15, 10]
assert root.sumTree() == 70
print(root.preOrder())
print(root.inOrder())
print(root.postOrder())
print(root.sumTree())


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# PROBLEM 4
def parse_file(file):
    if os.path.exists(file):
        reversed_lines = []
        with open(file, "r") as open_file:
            lines = open_file.readlines()

            num_lines = len(lines)
            num_words = 0
            num_characters = 0
            for line in lines:
                reversed_lines.append(line)
                num_words += len([word for word in line.split(" ") if word != '' and word != '\n'])
                num_characters += len(line)

            print("Total number of lines: " + str(num_lines))
            print("Total number of words: " + str(num_words))
            print("Total number of characters: " + str(num_characters))

        with open("reversed_lines.txt", "w") as write_file:
            while reversed_lines:
                write_file.write(reversed_lines.pop())

    else:
        print(file + " does not exist.")

print("\nProblem 4:")
# Given Test Case
# parse_file('sample.txt')

parse_file('test.txt')

# My Test Cases
"""
CASE 1:
INPUT:
input.txt (Three new line characters)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parse_file('input.txt')

OUTPUT:
Total number of lines: 3
Total number of words: 0
Total number of characters: 3

reversed_lines.txt:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


CASE 2:
INPUT:
input.txt - does not exist

parse_file('input.txt')

OUTPUT:
input.txt does not exist

reversed_lines.txt - does not exist (if it didn't exist previously)

CASE 3:
INPUT:
input.txt: (empty file)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parse_file('input.txt')

OUTPUT:
Total number of lines: 0
Total number of words: 0
Total number of characters: 0

reversed_lines.txt: (empty file)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


CASE 4:
INPUT:
input.txt (Three lines of only whitespaces)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Hello world!
   Lots of whitespace.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parse_file('input.txt')

OUTPUT:
Total number of lines: 2
Total number of words: 5
Total number of characters: 39

reversed_lines.txt:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Lots of whitespace.
   Hello world!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


CASE 5:
INPUT:
input.txt: (empty file)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file only has one line.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

parse_file('input.txt')

OUTPUT:
Total number of lines: 1
Total number of words: 6
Total number of characters: 28

reversed_lines.txt:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file only has one line.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
