queue = []  # Start with an empty queue

item = input("Add to queue: ").strip()  
if item:  # Only add non-empty input
    queue.append(item)
else:
    print("Invalid input. Queue not updated.")

print(queue)  # Print the updated queue
