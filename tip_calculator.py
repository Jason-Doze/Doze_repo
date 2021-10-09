
# The goal of this project is to make a tip calculator app in python and put together a new Github repo for it. To submit your project, you will simply submit the link to your Github repo on Canvas


# You should set up a public Github repo that contains your code, and a README.md file. This repo with your app will be part of your code portfolio from this class, so keep it neat, and make the README file look nice using markdown formatting. Be sure to give it a title, and provide a brief summary of what your code does, and how to run it. To submit your project, you will simply submit the link to your Github repo on Canvas. Your completed project will be part of your code portfolio on Github, so go ahead and make it look good, and feel free to put your own spin on it!

# Your app must run propely in python from the command line, and should not require any software or external libraries.
# Your tip calculator must be interactive and take user input at the command line. This means that your python code must respond appropriately based on what the user enters.

# Your code must be well-commented. Demonstrate how much you understand!
# This project is an individual one! You can talk to your classmates for ideas, but all code should be your own.


# You can always reference the course Github repo and use any lessons or challenges there to guide you
# Googling when you are stuck is encouraged! If you find a snippet of code on the internet you want to use, just make sure that you put a link in acknowledging the source, and comment it to make sure you understand it.

# Check in with others in the class, your TAs, and your instructors! Remember that the more proactive you are about seeking out resources, the easier it will be to get on track.

# The total bill (including tip)
# How much each person should pay (you can assume all people will split the bill evenly)
# Total bill including tip / amount of people paying the bill
# Assume there is a 10% sales tax. Don't forget to add this into the total bill!
# Note: your tip calculator should be able to handle a bill of any amount of many money, with any number of people splitting the bill, and with any tip percentage (including 0 tip)



# Tip calculator greeting
print()
print("Tip Calculator")
print()


# Bill cost input function receives total bill cost from user
input_bill_cost = float(input("What is the total cost of the bill?: $ "))
print(input_bill_cost)
print()


# Party size/ amount of people function receives number of patrons splitting the bill
input_amount_served = float(input("How many people will be splitting the bill?: "))
print(input_amount_served)
print()


# Tip Percentage input function receives tip percentage from patrons
input_tip_percentage = float(input("What percentage of tip would you like to leave?: "))
print(input_tip_percentage)
print()

# Sales tax applied will be 10%
sales_tax_calc = input_bill_cost * .10
print(f'The sales tax on this bill is {sales_tax_calc}')
print()


# Tip amount variable multiplies the bill and tip percentage, tip total variable converts tip amount to get the percentage 
tip_amount =  input_bill_cost * input_tip_percentage
tip_total = tip_amount / 100
print(f'The % tip calculation for this bill is: $ {tip_total}')
print()


# the total bill combines the bill, sales tax, and tip into a total cost required for payment
total_bill =  round(tip_total  + sales_tax_calc + input_bill_cost, 2)
print(f'The total bill for this meal including tip and %10 sales tax is: {total_bill}')
print()


# Bill per person variable calculates how much each person is responsible for paying when equally dividing the bill
bill_per_person = round(total_bill / input_amount_served,2)
print(f'The amount per person will be: $ {bill_per_person} each')
print()






