## input we need from the user 
# total rent 
# total food ordered for snacking 
# electricity bill
# charge per unit 
## the total amount u have to pay (output)

rent = int(input("Enter your hostel/flat rent =  "))
food = int(input("Enter the amount of food ordered ="))
electricity_bill = int(input("Enter the electricity bill = "))
charge_per_unit = int(input("Enter the charge per unit of electricity = ")) 
person = int(input("Enter the number of people sharing the bill = "))

total_electricity_bill = electricity_bill * charge_per_unit

total_amount = rent + food + total_electricity_bill
amount_per_person = total_amount / person
print("The total amount you have to pay is = ", total_amount)
print("The amount each person has to pay is = ", amount_per_person)


