# 07. Write a menu-driven program to implement the stack data structure.

stack = []

def push():
    item = input("Enter the item to push onto the stack: ")
    stack.append(item)
    print(f"Item '{item}' pushed onto the stack.")

def pop():
    if not stack:
        print("Stack is empty. Cannot pop.")
    else:
        item = stack.pop()
        print(f"Item '{item}' popped from the stack.")

def peek():
    if not stack:
        print("Stack is empty. Nothing to peek.")
    else:
        print(f"Top item on the stack: {stack[-1]}")

def display():
    if not stack:
        print("Stack is empty.")
    else:
        print("Stack contents:")
        for item in reversed(stack):
            print(item)

# Menu-driven program
while True:
    print("\nStack Operations Menu:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")