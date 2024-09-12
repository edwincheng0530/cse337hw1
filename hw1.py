from collections import Counter
import os
"""""
# Problem 1
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
        return True
    if len(keys) > 2:
        return False

    diff1 = abs(keys[0]-keys[1])*abs(lengthFrequency[keys[0]])
    diff2 = abs(keys[0]-keys[1])*abs(lengthFrequency[keys[1]])

    if diff1 <= 1 or diff2 <= 1:
        return 'YES'
    else:
        return 'NO'

print(isValid('aabbcd'))
print(isValid('aabbbcdddeefghi'))
print(isValid('abcdefghhgfedecba'))


# Problem 2
def isBalanced(string):
    stack = []
    open = {'{', '[', '('}
    close = {'}', ']', ')'}
    dict = {'}': '{', ']': '[', ')': '('}

    for bracket in string:
        if bracket in open:
            stack.append(bracket)
        elif bracket in close:
            poppedBracket = stack.pop()
            if poppedBracket != dict[bracket]:
                return 'NO'

    if len(stack) > 0:
        return 'NO'

    return 'YES'

print(isBalanced('{[()]}'))
print(isBalanced('{[(])}'))
print(isBalanced('{{[[(())]]}}'))
print(isBalanced('[{}]()'))
print(isBalanced('[{}()]'))
print(isBalanced('[{}]()'))


# Problem 3
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
"""
# Problem 4
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
                num_words += len(line.split(" "))
                num_characters += len(line)

            print("Total number of lines: " + str(num_lines))
            print("Total number of words: " + str(num_words))
            print("Total number of characters: " + str(num_characters))

        with open("reversed_lines.txt", "w") as write_file:
            while reversed_lines:
                write_file.write(reversed_lines.pop())

    else:
        print(file + " does not exist.")


parse_file('sample.txt')