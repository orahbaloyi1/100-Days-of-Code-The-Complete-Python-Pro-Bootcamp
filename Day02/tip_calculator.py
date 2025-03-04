# Print function to print welcome message
print("Welcome to the tip calculator!")

# Get the bill amount, tip percentage, and number of people
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# Calculate the total amount and per person
total_amount = tip / 100 * bill + bill
bill_per_person =  total_amount / people

print(f"This is the total bill ${round(total_amount, 2)}")

