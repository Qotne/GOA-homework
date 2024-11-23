# პაროლის სწორი მნიშვნელობა
correct_password = "group55"

# while ციკლი, რომელიც ითხოვს პაროლს
while True:
    user_password = input("გთხოვთ, შეიტანოთ პაროლი: ")
    
    # თუ პაროლი სწორია, გამოვდივართ ციკლიდან
    if user_password == correct_password:
        print("პაროლი სწორია! თქვენ წარმატებით შეიყვანეთ პაროლი.")
        break
    else:
        print("არასწორი პაროლი! სცადეთ ისევ.")
