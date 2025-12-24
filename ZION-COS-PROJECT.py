def calculate_tax(filing_status, income):
    # 2009 Tax Brackets
    brackets = [
        # Single Filers (Status 0)
        [ (8350, 0.10), (33950, 0.15), (82250, 0.25), (171550, 0.28), (372950, 0.33), (float('inf'), 0.35) ],
        # Married Filing Jointly or Qualifying Widow(er) (Status 1)
        [ (16700, 0.10), (67900, 0.15), (137050, 0.25), (208850, 0.28), (372950, 0.33), (float('inf'), 0.35) ],
        # Married Filing Separately (Status 2)
        [ (8350, 0.10), (33950, 0.15), (68525, 0.25), (104425, 0.28), (186475, 0.33), (float('inf'), 0.35) ],
        # Head of Household (Status 3)
        [ (11950, 0.10), (45500, 0.15), (117450, 0.25), (190200, 0.28), (372950, 0.33), (float('inf'), 0.35) ]
    ]

    if filing_status not in [0, 1, 2, 3]:
        return "Invalid filing status entered."

    taxable_brackets = brackets[filing_status]
    total_tax = 0
    remaining_income = income
    previous_limit = 0

    for limit, rate in taxable_brackets:
        if remaining_income > 0:
            taxable_amount = min(remaining_income, limit - previous_limit)
            total_tax += taxable_amount * rate
            remaining_income -= taxable_amount
            previous_limit = limit
        else:
            break

    return total_tax

# Prompt user for input
try:
    status = int(input("Enter filing status (0=Single, 1=Married Jointly, 2=Married Separately, 3=Head of Household): "))
    income_val = float(input("Enter taxable income: $"))
    tax_owed = calculate_tax(status, income_val)
    if isinstance(tax_owed, str):
        print(tax_owed)
    else:
        print(f"Your total tax owed is: ${tax_owed:,.2f}")
except ValueError:
    print("Invalid input. Please enter numerical values for status and income.")