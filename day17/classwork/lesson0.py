# დავიწყოთ მონაცემთა ტიპების მქონე სიით
data = [42, "გამარჯობა!", 3.14, True, None, [1, 2, 3], {"key": "value"}, (10, 20), {1, 2, 3}, b"bytes"]

# 1. პირველი სამი ელემენტის ცალკე გამოყვანა
print(data[0])  
print(data[1])  
print(data[2])  

# 2. მეორე სამი ელემენტის შეცვლა
data[3] = "Python"
data[4] = "JavaScript"
data[5] = "C++"

# 3. სიაში 5 ახალი ელემენტის დამატება
data.append("Rust")         
data.append("Go")           
data.append("Kotlin")       
data.append("Swift")      
data.append("TypeScript")   
# სიის საბოლოო შედეგის გამოყვანა
print("განახლებული სია:", data)


