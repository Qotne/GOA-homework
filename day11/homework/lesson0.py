# მომხმარებლისგან ქულის მიღება
score = int(input("შეიყვანეთ თქვენი ქულა: "))

# შეფასების განსაზღვრა
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"თქვენი შეფასება: {grade}")
