def calculate_charges():
    print("--Welcome To The Water Charges Calculator--")
    yearly_household_consumption = int(input("\nHow many liters did you use this year: "))
    number_of_adults = int(input("Enter with the quantity of adults in our house: "))
    number_of_children = int(input("Enter with the quantity of children in our house: "))


    # Calculating the charge free limit and its rules
    charge_free_limit = 213000 # Standard limit

    if number_of_adults >= 5:
        charge_free_limit += 30000
        if number_of_children >= 3:
            charge_free_limit += 5000 * (number_of_children - 2)

    elif number_of_adults >= 3:
        charge_free_limit += 20000
        if number_of_children >= 3:
            charge_free_limit += 7000 * (number_of_children - 2)


    # Calculating total charge and its rules
    charge_rate_litre = 3.70
    total_charge = (yearly_household_consumption - charge_free_limit) * charge_rate_litre
    if total_charge < 0:
        total_charge = 0

    print(f"\nYour yearly usage was: {yearly_household_consumption:,.2f} litres."
        f"\nYour Charge Free Limit is: {charge_free_limit:,} litres."
        f"\nYour Charge is: €{total_charge:,.2f}")

if __name__ == "__main__":
    calculate_charges()