first_answer = int(input("Choose a path (1, 2, or 3): "))

if first_answer == 1:
    print("\nYou selected the first path.")
    second_answer = int(input("Choose an option (1 or 2 or 3): "))
    if second_answer == 1:
        print("You chose the 1-1")
        third_answer = int(input("Make a final decision (1 or 2: "))
        if third_answer == 1:
            print("You chose the 1-1-1.")
    elif second_answer == 2:
        print("You chose the 2-1.")
        third_answer = int(input("Make a final decision (1 or 2: "))
        if third_answer == 1:
            print("You chose the 1-2-1.")
    elif second_answer == 3:
        print("You chose the 3-1.")
        third_answer = int(input("Make a final decision (1 or 2: "))
        if third_answer == 1:
            print("You chose the 1-3-1.")
elif first_answer == 2:
    print("\nYou selected the second path.")
    second_answer = int(input("Choose an option (1 or 2 or 3): "))
    if second_answer == 1:
        print("You chose the 1-2")
    elif second_answer == 2:
        print("You chose the 2-2.")
    elif second_answer == 3:
        print("You chose the 3-2.")
elif first_answer == 3:
    print("\nYou selected the third path.")
    second_answer = int(input("Choose an option (1 or 2 or 3): "))
    if second_answer == 1:
        print("You chose the 1-3")
    elif second_answer == 2:
        print("You chose the 2-3.")
    elif second_answer == 3:
        print("You chose the 3-3.")
else:
    print("\nInvalid choice. Please select 1, 2, or 3.")
