monthly_income = input("Enter your monthly income: ")
total_monthly_expense = input("Enter your total monthly expenses: ")

monthly_savings = monthly_income - total_monthly_expense

Assume a simple annual interest rate of 5%.
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are ", monthly_savings)
print("Projected savings after one year, with interest, is: ",projected_savings)