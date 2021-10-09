# Tip Calculator



## Basic Syntax

This tip calculator takes 3 inputs from the user. The total price of the bill, the tip amount from the customer, and the amount of people that will be splitting the bill. The calculator adds a 10% sales tax to every calculation and ouputs the total bill amount including tip, sales tax and the total cost per customer based on how many patrons will be splitting the bill. All of these outputs are expressed within a string for clarity.

<!-- ### Heading

# H1
## H2
### H3

### Bold -->

1. Tip calculator greeting
2. Bill cost input function receives total bill cost from user
3. Party size/ amount of people function receives number of patrons splitting the bill
4. Tip Percentage input function receives tip percentage from patrons
5. Sales tax applied will be 10%
6. Tip amount variable multiplies the bill and tip percentage, tip total variable converts tip amount to get the percentage 
7. the total bill combines the bill, sales tax, and tip into a total cost required for payment
8. Bill per person variable calculates how much each person is responsible for paying when equally dividing the bill



### Code

print()
print("Tip Calculator")
print()


input_bill_cost = float(input("What is the total cost of the bill?: $ "))
print(input_bill_cost)
print()


input_amount_served = float(input("How many people will be splitting the bill?: "))
print(input_amount_served)
print()


input_tip_percentage = float(input("What percentage of tip would you like to leave?: "))
print(input_tip_percentage)
print()


sales_tax_calc = input_bill_cost * .10
print(f'The sales tax on this bill is {sales_tax_calc}')
print()


tip_amount =  input_bill_cost * input_tip_percentage
tip_total = tip_amount / 100
print(f'The % tip calculation for this bill is: $ {tip_total}')
print()


total_bill =  round(tip_total  + sales_tax_calc + input_bill_cost, 2)
print(f'The total bill for this meal including tip and %10 sales tax is: {total_bill}')
print()


bill_per_person = round(total_bill / input_amount_served,2)
print(f'The amount per person will be: $ {bill_per_person} each')
print()


<!-- ### Horizontal Rule

---

### Link


### Table

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

### Fenced Code Block

### Footnote

Here's a sentence with a footnote. [^1]

[^1]: This is the footnote.

### Heading ID

### My Great Heading {#custom-id}

### Definition List

term
: definition

### Strikethrough

~~The world is flat.~~

### Task List -->
<!-- 
- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media -->

