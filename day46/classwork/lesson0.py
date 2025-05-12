def repeats(arr):
    return sum(x for x in arr if arr.count(x) == 1)

def litres(time):
    return int(time // 2)

def cat_mouse(x):
    return "Caught!" if x.index('m') - x.index('C') <= 4 else "Escaped!"