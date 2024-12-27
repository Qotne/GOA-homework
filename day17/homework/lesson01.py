numbers = []
while True:
    number = input("შეიყვანეთ რიცხვი (დამთავრებისთვის დააჭირეთ Enter): ")
    if number == "":
        break
    numbers.append(int(number))

print(f"შეიყვანეთ {len(numbers)} რიცხვი.")
