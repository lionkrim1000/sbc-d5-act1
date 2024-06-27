numbers = []

while True:
    user_input = input("Enter 'add', 'display', 'naa', 'wala', or 'done': ").strip().lower()

    if user_input == 'done':
        break
    elif user_input == 'add':
        try:
            number = int(input("Enter a number to add: "))
            numbers.append(number)
            print(f"Added {number} to the list.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif user_input == 'display':
        print("Current list:", numbers)
    elif user_input == 'naa':
        if numbers:
            print(f"Pop: {numbers.pop()}")
        else:
            print("List is empty.")
    elif user_input == 'wala':
        if numbers:
            print(f"Pop: {numbers.pop(0)}")
        else:
            print("List is empty.")
    else:
        print("Invalid input. Please enter 'add', 'display', 'naa', 'wala', or 'done'.")

print("Final list:", numbers)
print("Exiting program.")
