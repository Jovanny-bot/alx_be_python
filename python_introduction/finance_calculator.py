montly_income = float (input("Enter your montly income:"))
montly_expenses =  float (input("Enter your total montly expenses:"))
montly_savings= montly_income-montly_expenses
Interest_rate = 0.005
Project_annual_savings= montly_savings *12 + (montly_savings*12*Interest_rate)
print(f"Your monthly savings are {montly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is:{Project_annual_savings:.2f}.")







