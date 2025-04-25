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

def printer_error(s):
    errors = 0
    total = len(s)

    for letter in s:
        if letter not in "abcdefghijklm":
            errors = errors + 1

    fraction = str(errors) + "/" + str(total)
    return fraction