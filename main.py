#Rahhim Adeem
# Task 1: Define a function that accepts and returns the list sorted in ascending order without using the built-in sorted() function.

def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

# Task 2: Implement a class called CustomStack that simulates a stack with the following methods:
# push(item) to add an item to the stack.
# pop() to remove and return the top item from the stack.
# is_empty() to check if the stack is empty.
# peek() to return the top item without removing it.

class CustomStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

# Task 3: Write a function that reads a string and returns a dictionary with the frequency count of each character in the string.

def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

