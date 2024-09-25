
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses =  float(input("Enter your total monthly expenses: "))

monthly_savings= monthly_income - monthly_expenses
interest_rate = 0.005

project_annual_savings = monthly_savings * 12 + (monthly_savings * 12 * interest_rate)
print(f"Your monthly savings are {monthly_savings:.2f}")
print(f"Projected savings after one year, with interest, is: ${project_annual_savings:.2f}.")







