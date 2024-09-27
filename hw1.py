from collections import Counter

# PROBLEM 1
def isValid(string):
    charFrequency = {}
    # Count frequency of each unique character found in string and store in a dictionary
    charFrequency = Counter(string)
    # Create a dictionary where key is frequency that a character appears and value is the number of times this frequency exists in the string
    lengthFrequency = {}
    for frequency in charFrequency.values():
        if frequency in lengthFrequency:
            lengthFrequency[frequency] += 1
        else:
            lengthFrequency[frequency] = 1

    keys = list(lengthFrequency.keys())
    # If all characters have the same frequency, it is a valid string
    if len(keys) == 1:
        return 'YES'
    # If there are more than 2 different frequencies, then it will be impossible for the string to be valid
    # as we are only capable of deleting one of these frequencies in the best case scenario
    if len(keys) > 2:
        return 'NO'

    # If we are here, that means there are exactly 2 frequencies - 
    # if one of these frequencies represents a single unique character, we can remove it and the string is valid  
    if((lengthFrequency[keys[0]] == 1 and keys[0] == 1)
       or (lengthFrequency[keys[1]] == 1 and keys[1] == 1)):
        return 'YES'
    
    # Remove a character from the largest occuring frequency and update the lengthFrequency dictionary
    largestFreq = max(keys[0], keys[1])
    lengthFrequency[largestFreq] -= 1

    # After removing a character, there should only be one length frequency left
    return 'YES' if lengthFrequency[largestFreq] == 0 and (largestFreq-1) in keys else 'NO'

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
        # If the character is an open bracket, push it onto stack
        if bracket in open:
            stack.append(bracket)
        # If the character is a closing bracket, pop the stack
        # If the closing bracket doesn't match opening bracket or stack is empty, return NO
        elif bracket in close:
            if stack:
                poppedBracket = stack.pop()
            else:
                return 'NO'
            if poppedBracket != dict[bracket]:
                return 'NO'

    # If stack still has elements, the string isn't balanced - retur NO
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

        # If preOrder, add to list before traversing to its left and right child respectively
        if order == 1:
            list.append(node.label)
        self.recursive(node.leftChild, list, order)

        # If inOrder, add to list after traversing to the left but before going to the right child
        if order == 2:
            list.append(node.label)
        self.recursive(node.rightChild, list, order)
        
        # If postOrder, add to list after traversing to its left and right child
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
    try:
        reversed_lines = []
        with open(file, "r") as open_file:
            lines = open_file.readlines()

            num_lines = len(lines)
            num_words = 0
            num_characters = 0
            # Add each line to LIFO stack
            for line in lines:
                reversed_lines.append(line)
                # Add number of words that exist on the current line, ignoring new line character and empty strings
                num_words += len([word for word in line.split(" ") if word != '' and word != '\n'])
                # Add number of characters
                num_characters += len(line)

            print("Total number of lines: " + str(num_lines))
            print("Total number of words: " + str(num_words))
            print("Total number of characters: " + str(num_characters))

        with open("reversed_lines.txt", "w") as write_file:
            # Write to new file while elements still exist on LIFO stack
            while reversed_lines:
                write_file.write(reversed_lines.pop())

    except FileNotFoundError:
        print(file + " does not exist.")
    except Exception as e:
        print("Exception occured: " + e)

print("\nProblem 4:")
# Given Test Case
parse_file('sample.txt')


# My Test Cases
parse_file('input1.txt')
"""
OUTPUT:
Total number of lines: 3
Total number of words: 0
Total number of characters: 3

reversed_lines.txt:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
parse_file('input2.txt')
"""
OUTPUT:
input.txt does not exist

reversed_lines.txt - does not exist (if it didn't exist previously)
"""
parse_file('input3.txt')
"""
OUTPUT:
Total number of lines: 0
Total number of words: 0
Total number of characters: 0

reversed_lines.txt: (empty file)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
parse_file('input4.txt')
"""
OUTPUT:
Total number of lines: 2
Total number of words: 5
Total number of characters: 39

reversed_lines.txt:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   Lots of whitespace.
   Hello world!

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
parse_file('input5.txt')
"""
OUTPUT:
Total number of lines: 1
Total number of words: 6
Total number of characters: 28

reversed_lines.txt:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file only has one line.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""