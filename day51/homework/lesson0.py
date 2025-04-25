def open_or_sinior(data):
    output = []
    for person in data:
        age = person[0]
        handicap = person[1]
        if age >= 55 and handicap > 7:
            output.append("senior")
        else:
            output.append("open")
    return output

def find_next_square(sq):
    if  (sq ** 0.5) % 1 == 0:
        return ((sq ** 0.5) + 1) ** 2
    return -1

def row_sum_odd_numbers(n):
    