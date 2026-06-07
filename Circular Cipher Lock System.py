# 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9
# 9 wraps back to 0

import random

# Welcome the user
print("Welcome to a Lock System in Python!") 

# define the core logic
def findDial(target, current):
        if ((target - current) % 10) >= ((current - target) % 10):
            direction = "Clockwise"
            steps = ((current - target) % 10)
            current = target 
        else:
            direction = "Anti-Clockwise"
            steps = ((target - current) % 10)
            current = target
        return direction, steps, current

while True: 
    strPassword = list(input("\nEnter your password: "))
    try:
        password = list(map(int, strPassword))
    except ValueError:
        print("Only put integers for password.")
        continue

    current = random.randint(0, 9)

    # Main For loop
    for i in range(1, len(password)+1):
        print(f"\nYour current index: {i}")

        print("Your current dial position:", current)

        try:
            target = int(input("Enter target number: "))
        except ValueError:
            print("Choose only integers for target number.")
            break

        if target < 0 or target > 9:
            print("Choose between 0-9.")
            break
        
        # Use that def logic
        direction, steps, current = findDial(target, current)

        # Show the data
        print(f"dir: {direction}, steps: {steps}, current dial position: {current}, target was: {target}")
        if target == password[i-1]:
            print("\nCorrect Password!")
            continue
        else:
            print("Wrong Password!")
            break