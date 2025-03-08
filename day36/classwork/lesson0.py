def bool_to_word(boolean):
    return "Yes" if boolean else "No"   

def grow(arr):
    result = 1  
    for num in arr:  
        result *= num 
    return result  

    