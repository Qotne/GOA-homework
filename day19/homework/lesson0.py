# სიის შექმნა
numbers = []
print("შეიყვანეთ 10 რიცხვი:")

for _ in range(10):  # 10-ჯერ ვთხოვთ მომხმარებელს რიცხვის შეყვანას
    while True:
        try:
            num = int(input("რიცხვი: "))
            numbers.append(num)
            break
        except ValueError:
            print("შეიყვანეთ მხოლოდ რიცხვი!")

print("\nშექმნილი სია:", numbers)

# უდიდესი რიცხვის პოვნა სიაში
if numbers:  # ვამოწმებთ, სია ხომ არ არის ცარიელი
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    print("\nუდიდესი რიცხვი სიაშია:", max_num)
else:
    print("\nსიაში ელემენტები არ არის.")

# ელემენტის წაშლა სიიდან
try:
    to_remove = int(input("\nშეიყვანეთ წასაშლელი რიცხვი: "))
    if to_remove in numbers:
        numbers.remove(to_remove)
        print("განახლებული სია წაშლის შემდეგ:", numbers)
    else:
        print("რიცხვი სიაში არ არის.")
except ValueError:
    print("შეიყვანეთ მხოლოდ რიცხვი!")

# სიის საპირისპირო მიმდევრობით ჩაწერა
if numbers:
    reversed_list = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i])
    print("\nსია საპირისპირო წესით:", reversed_list)
else:
    print("\nსიაში ელემენტები არ არის.")

# ელემენტის ძებნა სიაში
try:
    search_num = int(input("\nშეიყვანეთ საძიებელი რიცხვი: "))
    if search_num in numbers:
        print(f"რიცხვი {search_num} სიაში არის.")
    else:
        print(f"რიცხვი {search_num} სიაში არ არის.")
except ValueError:
    print("შეიყვანეთ მხოლოდ რიცხვი!")
