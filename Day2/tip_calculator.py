# Day2 for 100Days4Python
# Project for Day2

print("Welcome to the tip calculator!")
total = float(input("What was the total bill? >>> $"))
tip_ratio = float(input("How much tip would you like to give? 10%, 12%, or 15%? >>> ")[:2]) / 100.0
n_people = int(input("How many people to split the bill? >>> "))
result = (total * (1 + tip_ratio)) / n_people

print(f"Each person should pay: ${result:.2f}")