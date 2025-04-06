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

