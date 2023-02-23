import math

investment_choice =  input("""Choose either "investment" or "bond" from the menu below to proceed:\n  
investment -   to calculate the amount of interest you\'ll earn on interest
bond -  to calculate the amount you\'ll have to pay on a home loan
\nPlease enter your choice:""").lower() # Asks user to enter their choice of investment or bond 

if investment_choice == 'investment': # Deteremined if the user chooses the investment option
    invest_deposit = float(input('Please enter the amount of money that you\'ll deposit:\n')) # asks user to enter the amount they wish to deposit
    interest_percent = float(input('Please enter your interest rate as a number not percentage:\n')) # asks user to enter the interest rate
    interestRate_percent = interest_percent/100 # divides the users interest rate input by 100 so it is turned into a percentage
    num_years = int(input('Please enter the number of years you plan on investing for:\n')) # asks user to enter the amount of years they plan on investing for
    type_of_interst = input('Please enter wheater you will be taiking "compound" or "simple" interest:\n').lower() # asks user to choose between simple or compound

    if type_of_interst == 'simple': # deteremines wheater the user entered simple
        final_amount_s = invest_deposit * (1+interestRate_percent*num_years) # calculates how much interest the user makes
        print(f'Your total is {round(final_amount_s, 2)}') # prints out the final amount and rounds it off to two decimal places

    if type_of_interst == 'compound': # deteremines wwheater the user entered compound
        final_amount_c = invest_deposit*math.pow((1+interestRate_percent),num_years) # calculates the compound interest
        print(f'Your total is {round(final_amount_c, 2)}') # prints out the final amount and rounds it off to two decimal places


elif investment_choice == 'bond': # determines if user chooses the bond option
    house_value = float(input('Please enetr the value of the house:\n')) # ask user to enter value of the house 
    Bond_Interest_Rate = float(input('Please enter the interest rate:\n')) # ask user to enter the interest rate 
    Monthly_Payment = float(input('Please enter the amount of months you plan on paying for the house:\n')) # asks the user to enter the amount of months they plan on paying off the house
    Final_Bond_InterestRate = Bond_Interest_Rate/12 # divides the interest rate by 12
    Bond_Total = (Final_Bond_InterestRate*house_value)/(1-(1+Final_Bond_InterestRate)**(-Monthly_Payment)) # calculates the monthly bond
    print(f'Your total repayment comes to {round(Bond_Total, 2)} a month') # prints out the final amount and rounds it off to two decimal places

else: # deteremines if the user did not enter bond or investment
    print('You have not entered "bond" or "investment"\n Please try again') # send out error message to user if put in the wrong input