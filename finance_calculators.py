#A short script to caluculate returns on various types of investments

#Import maths to use functions unavailable otherwise for later caluclations
import math

#Ask the user which type of investment they are after
#.lower is used to allow the user to input their choice in the manner they choose
selection = input("""Investment - to calculate the amount of interest you'll earn on your investment
Bond - to calculate the amount you'll have to pay on a home loan 

Enter either 'investment' or 'bond' from the menu above to proceed: """).lower()

#First branch is if investment is selected
if selection == "investment":
    #Ask for various data from user for caluclations
    deposit = float(input("Please enter the amount of money you wish to deposit: "))
    #Interest rate is divided by 100 as it's a percentage
    int_rate = float(input("Please enter the interest rate as a percentage without the % symbol: "))/100
    year = int(input("Please enter the number of years you would like to invest for: "))
    interest = input("Would you like simple or compound interest? ").lower()
    #A nested if statement for when simple interest is selected
    if interest == "simple":
        #Caluculation for simple interest
        amount = deposit*(1+int_rate*year)
        print("The expected amount is £" + str(round(amount,2)))
    #The next branch for compound interest
    elif interest == "compound":
        #Caluculation for compound interest
        amount = deposit*math.pow(1+int_rate,year)
        print("The expected amount is £" + str(round(amount,2)))
    #Error route in case anything else is typed in
    elif interest != "simple" or "compound":
        print("Please type in either simple or compound please: ")
    #Second error route to catch any other errors
    else:
        print("Unknown error, please try again")
#Second choice if bond is selected
elif selection == "bond":
    #Ask for various data from user for caluclations
    value = int(input("Please enter the value of the property as a whole number: "))
    int_rate = float(input("Please enter the interest rate as a percentage without the % symbol: "))/(100*12)
    months = int(input("Please enter the amount of months to repay the bond: "))
    #Calculation for bond
    amount = (int_rate*value)/(1-(1+int_rate)**(-months))
    print("The amount to repay monthly is £" + str(round(amount,2)))
#Error route for something else typed in outside of predicated choices
elif selection != "investment" or "bond":
    print("Please either type in investment or bond")
#Final error route for something somehow missed
else:
    print("Unknown error, please try again")