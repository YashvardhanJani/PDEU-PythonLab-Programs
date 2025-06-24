# 08. Write a menu-driven program to implement the Queue data structure.

queue = []

def enqueue():
    item = input("Enter the item to enqueue into the queue: ")
    queue.append(item)
    print(f"Item '{item}' added to the queue.")

def dequeue():
    if not queue:
        print("Queue is empty. Cannot dequeue.")
    else:
        item = queue.pop(0)
        print(f"Item '{item}' removed from the queue.")

def peek():
    if not queue:
        print("Queue is empty. Nothing to peek.")
    else:
        print(f"Front item in the queue: {queue[0]}")

def display():
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue contents:")
        for item in queue:
            print(item)

# Menu-driven program
while True:
    print("\nQueue Operations Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display Queue")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")