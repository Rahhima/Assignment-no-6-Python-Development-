import main
# test_main.py

from main import sort_list, CustomStack, char_frequency
def test_sort_list():
    # Test case 1: Sorting a list of numbers
    numbers = [5, 2, 8, 1, 3]
    sorted_numbers = sort_list(numbers)
    assert sorted_numbers == [1, 2, 3, 5, 8]

    # Test case 2: Sorting an empty list
    empty_list = []
    sorted_empty_list = sort_list(empty_list)
    assert sorted_empty_list == []

    # Test case 3: Sorting a list with duplicates
    numbers_with_duplicates = [5, 2, 8, 1, 3, 3, 2]
    sorted_numbers_with_duplicates = sort_list(numbers_with_duplicates)
    assert sorted_numbers_with_duplicates == [1, 2, 2, 3, 3, 5, 8]

def test_custom_stack():
    # Test case 1: Push and pop operations
    stack = CustomStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1

    # Test case 2: Is empty operation
    empty_stack = CustomStack()
    assert empty_stack.is_empty() == True
    empty_stack.push(1)
    assert empty_stack.is_empty() == False

    # Test case 3: Peek operation
    stack = CustomStack()
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 2
    assert stack.pop() == 2
    assert stack.peek() == 1

    # Test case 4: Pop from an empty stack
    empty_stack = CustomStack()
    assert empty_stack.pop() == None

    # Test case 5: Peek from an empty stack
    empty_stack = CustomStack()
    assert empty_stack.peek() == None

def test_char_frequency():
    # Test case 1: Frequency count of characters in a string
    string = "hello world"
    frequency = char_frequency(string)
    assert frequency == {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

    # Test case 2: Frequency count of characters in an empty string
    empty_string = ""
    frequency = char_frequency(empty_string)
    assert frequency == {}