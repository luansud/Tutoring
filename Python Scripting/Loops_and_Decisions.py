name = "Lua"
age = input("Enter your age: ")
age = int(age)


if age >= 18:
    print(f"{name} is an adult")

    while True:
        driver_license = input("Do you have a driver's license? (yes/no): ").lower()
        if driver_license == "yes":
            print(f"{name} can drive a car.")
            break
        elif driver_license.lower() == "no":
            print(f"{name} cannot drive a car.")
            break
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")
            


elif age <= 17 and age >= 12:
    print(f"{name} is a Young boy")
    high_school = input("Are you in high school? (yes/no): ")
    if high_school.lower() == "yes":   
        print(f"{name} is attending high school.")
    elif high_school.lower() == "no":
        print(f"{name} is not attending high school.")


elif age < 12 and age >= 4:
    print(f"{name} is a Child")
    kingergarten = input("Are you in kindergarten? (yes/no): ")
    if kingergarten.lower() == "yes":   
        print(f"{name} is attending kindergarten.")
    elif kingergarten.lower() == "no":
        print(f"{name} is not attending kindergarten.")


elif age < 4 and age >= 1:
    print(f"{name} is a Toddler")
elif age < 1:
    print(f"{name} is an baby")