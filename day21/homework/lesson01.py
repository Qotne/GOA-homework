
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

numbers.append(100)
print("After adding 100:", numbers)

numbers.insert(0, 5)
print("After adding 5 at the start:", numbers)

numbers.remove(30)
print("After removing 30:", numbers)

numbers.reverse()
print("After reversing the list:", numbers)

index_of_50 = numbers.index(50)
print("Index of 50:", index_of_50)

count_of_20 = numbers.count(20)
print("Count of 20:", count_of_20)
