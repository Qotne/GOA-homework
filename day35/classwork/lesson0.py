print(7425 / 550)

bill_amount = float(input())
tip = bill_amount * 0.2
print(tip)

weight = float(input())
height = float(input())

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obesity")

    def search(text, word):
    if word in text:
        result = "Word found"
    else:
        result = "Word not found"
    return result







