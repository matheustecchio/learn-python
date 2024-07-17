def calculate_tax():
    print("--Welcome To The Tax Calculator--")
    # User inputs: salary, number of children, and monthly mortgage payments
    salary = int(input("Enter your salary: "))
    children = int(input("Enter the amount of children you have: "))
    mortgage = int(input("Enter amount of monthly mortgage payments: "))

    # Step 1: Determine the tax-free allowance (TFA)
    if children == 0 or mortgage < 150:
        tfa = 0
    else:
        if children <= 3:
            if mortgage < 300:
                tfa = 237
            else:
                tfa = 275
        else:
            tfa = 305

    # Step 2: Calculate the taxable income
    taxable_income = salary - tfa

    # Step 3: Apply the tax rates
    if taxable_income <= 35800:
        tax_due = taxable_income * 0.20
    else:
        tax_due = (35800 * 0.20) + ((taxable_income - 35800) * 0.40)

    tax_due = round(tax_due)

    # Print the results
    print("Tax due:\u20AC", tax_due, "Total allowance:\u20AC", tfa)
    print("Total tax payed: \u20AC", tax_due - tfa)


# Function to calculate monthly pay based on years worked, sales region, monthly sales, and mileage
def monthly_pay():
    print("--Welcome To The Monthly Pay Calculator--")
    # User inputs: years worked, sales region, monthly sales, and mileage
    years_worked = int(input("Enter the amount of years worked: "))
    sales_region = int(input("Which region are you in 1.SW, 2.MW, 3.NW, 4.SE, 5.ME, 6.NE: "))
    monthly_sales = int(input("Enter total sales within this month: "))
    mileage = int(input("Enter amount of mileage: "))

    # Define commission rates based on years of service and sales region
    if years_worked >= 5 and sales_region >= 1 and sales_region <= 3:
        commission_rate = 0.04
        if mileage > 2000:
            commission_rate += 0.003
    elif years_worked >= 5 and sales_region >= 4 and sales_region <= 6:
        commission_rate = 0.03
        if mileage > 3000:
            commission_rate += 0.005
    elif sales_region >= 1 and sales_region <= 3:
        commission_rate = 0.035
        if mileage > 2000:
            commission_rate += 0.003
    elif sales_region >= 4 and sales_region <= 6:
        commission_rate = 0.025
        if mileage > 3000:
            commission_rate += 0.005

    # Assuming no basic salary defined here
    # Calculate total monthly pay and commission earned
    total_monthly_pay = commission_earned = monthly_sales * commission_rate

    # Print the total monthly pay and commission earned
    print("Total monthly pay:", round(total_monthly_pay))
    print("Total commission:", round(commission_earned))

if __name__ == "__main__":
    calculate_tax()
    monthly_pay()
