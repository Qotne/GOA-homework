def solution(text, ending):
     return text[-len(ending):] == ending

def digitize(n):
    return list(map(int, str(n)))[::-1]

def century(year):
    return (year + 99) // 100

def litres(time):
    return int(time // 2)


