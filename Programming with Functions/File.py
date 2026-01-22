from datetime import datetime
import math

car = "Toyota"

print(car)


with open("wordlist.txt", mode="wt") as profile_file:
    datetime_now = datetime.now()
    print(f"Date: {datetime_now:%Y-%m-%d}", file=profile_file)
    print(f"Name: {car}", file=profile_file)