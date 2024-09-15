montly_income = float (input("Enter your montly income"))
montly_expenses = float (input("Enter your montly expenses"))
Your_montly_savings= montly_income-montly_expenses
Annual_savings = Your_montly_savings* 12
Interest_rate = 0.005
Project_annual_savings= Annual_savings+ (Annual_savings*Interest_rate)
print(f"Your monthly savings are ${Your_montly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${Project_annual_savings:.2f}.")







