def between(a,b):
     return list(range(a,b+1))

def solution(string):
    return string[::-1]

def boolean_to_string(b):
    return str(b)

def quarter_of(month):
    if 1 <= month <= 3:
        return 1
    elif 4 <= month <= 6:
        return 2
    elif 7 <= month <= 9:
        return 3
    else:
        return 4