import math
from datetime import datetime

# Have the user enter a tire width in mm.
#width = float(input("Enter the width of the tire in mm (ex 205): "))
# Have the user enter the aspect ratio.
#aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
# Have the user enter the diameter of the wheel in inches.
diameter = 0

# Calculate and display the tire's volume.
#print("The approximate volume is 24.09 liters")

# Log the information in a text file.
# current date (Do NOT include time)
# width of the tire
# aspect ratio of the tire
# diameter of the wheel
# volume of the tire (rounded to two decimal places)

print(f"{datetime.now():%Y-%m-%d}")

#open("volumes.txt", mode="at") 
#open("volumes.txt", mode="wt")
#open("volumes.txt", mode="rd")

print("Love and python walk together", sep=" ")

#print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)

name = "Allison"
age = 19
hobby = "reading"
city = "Issaquah"

with open("profile.txt", mode="wt") as profile_file:
    datetime_now = datetime.now()
    print(f"Date: {datetime_now:%Y-%m-%d}", file=profile_file)
    print(f"Name: {name}", file=profile_file)
    print(f"Age: {age}", file=profile_file)
    print(f"Hobby: {hobby}", file=profile_file)
    print(f"City: {city}\n", file=profile_file)

