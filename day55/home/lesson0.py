def small_enough(array, limit):
    for number in array:
        if number > limit:
            return False
    return True

def sum_two_smallest_numbers(numbers):
    if numbers[0] < numbers[1]:
        smallest = numbers[0]
        second_smallest = numbers[1]
    else:
        smallest = numbers[1]
        second_smallest = numbers[0]
    for number in numbers[2:]:
        if number < smallest:    
            second_smallest = smallest
            smallest = number  
        elif number < second_smallest:
            second_smallest = number 
    return smallest + second_smallest  

def is_square(n):    
    if n < 0:
        return False

    root = n ** 0.5

    if root == int(root):
        return True
    else:
        return False
    
def password(st):
    if len(st) < 8:
        return False

    if not any(char.isupper() for char in st):
        return False

    if not any(char.islower() for char in st):
        return False

    if not any(char.isdigit() for char in st):
        return False
    return True
