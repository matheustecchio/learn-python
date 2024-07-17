def calculate_property_tax():
    print("--Welcome To The School Transport Calculator--\n")
    print("What is your property valuation:")
    property_valuation = float(input())
    int("What is your monthly mortgage payment: ")
    monthly_mortgage_payment = float(input())
    print("Where is your home located: ")
    location = input()
    # Calculate allowances
    mortgage_allowance = 3 * monthly_mortgage_payment
    location_allowance = 0
    if location == "Dublin":
        if property_valuation < 500000:
            location_allowance = 0.154 * property_valuation
    else:
        location_allowance = 0.082 * property_valuation
    total_allowances = mortgage_allowance + location_allowance

   # Calculate tax
    tax_due = 0
    if property_valuation <= 300000:
      tax_due += property_valuation * 0.002
    elif property_valuation <= 500000:
      tax_due += 300000 * 0.002 + (property_valuation - 300000) * 0.0025
    elif property_valuation <= 1000000:
      tax_due += 300000 * 0.002 + 200000 * 0.0025 + (property_valuation - 500000) * 0.003
    else:
      tax_due += 300000 * 0.002 + 200000 * 0.0025 + 500000 * 0.003 + (property_valuation -
                                                                          1000000) * 0.0035
    print("Tax due: €", int(tax_due))
    print("Total allowances: €", "%.2f" % total_allowances)

if __name__ == "__main__":
    calculate_property_tax()

