"""Answers to the pre-work Python questions."""
def hello_name(user):
    """Function to greet the input user."""
    print("hello_" + user + "!")

# hello_name test cases
print()
print("hello_name test cases")

hello_name("Matthew")
hello_name("Erika")

print()

def print_hundred_odd():
    """Print first 100 odd numbers"""
    current_number = 1
    first_hundred_odd = []

    while len(first_hundred_odd) < 100:
        first_hundred_odd.append(current_number)
        current_number += 2
    
    print(first_hundred_odd)
    return first_hundred_odd

# print_hundred_odd test cases
print("print_hundred_odd test cases")
test = print_hundred_odd()
print(len(test))
print()

def max_num_in_list(a_list):
    """Function to return the max number in a given list"""
    # Handle case if list is empty
    if not a_list:
        return None
    
    # Initialize max num
    max = a_list[0]

    # Loop through list to update max
    for num in a_list:
        if num > max:
            max = num

    return max


# max_num_in_list test cases
print("max_num_in_list test cases")
test_list1 = [1,3,2,4,5,6,7,4,3,38,3,5]
print(max_num_in_list(test_list1))
print()

def is_leap_year(a_year):
    """Function to determine if input year is a leap year."""
    if a_year % 400 == 0:
        return True
    elif a_year % 4 == 0 and not a_year % 100 == 0:
        return True
    else:
        return False

# is_leap_year test cases
print("is_leap_year test cases")
print(is_leap_year(2000))
print(is_leap_year(2012))
print(is_leap_year(3000))
print()

def is_consecutive(a_list):
    """Determines if the given list contains consecutive numbers."""
    if not a_list:
        return False

    for i in range(1, len(a_list)):
        if a_list[i] != a_list[i - 1] + 1:
            return False

    return True

# is_consecutive test cases
print("is_consecutive test cases")
test1 = [3,4,5,6,7,8,9]
test2 = [3,4,6,7,8,9]
print(is_consecutive(test1))
print(is_consecutive(test2))
