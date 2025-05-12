def mouth_size(animal): 
    return "small" if animal.lower() == "alligator" else "wide"

def past(h, m, s):
    return (h * 3600000) + (m * 60000) + (s * 1000)

def replace_exclamation(st):
     return st.translate(str.maketrans("aeiouAEIOU", "!!!!!!!!!!"))

def count_positives_sum_negatives(arr):
    if not arr: 
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    for num in arr:
        if num > 0:
            count_positives += 1
        elif num < 0:
            sum_negatives += num
    
    return [count_positives, sum_negatives]
