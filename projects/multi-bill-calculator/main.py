import water_charges
import school_transport
import TFAandMonthlyPay
import property_tax

# Display the menu
def menu():
    while(True):
        print("\n--Welcome To The Multi-Bill Calculator Menu--")
        print("_" * 35)
        print("1. Tax")
        print("2. Monthly Pay for Sales Employees")
        print("3. Water Charges")
        print("4. Property Tax")
        print("5. School Transport")
        print("0. Exit")
        print("_" * 35)
        option = int(input("Choose an option (0-5): "))
        print("\n")

        match option:
            case 1:
                TFAandMonthlyPay.calculate_tax()
            case 2:
                TFAandMonthlyPay.monthly_pay()
            case 3:
                water_charges.calculate_charges()
            case 4:
                property_tax.calculate_property_tax()
            case 5:
                school_transport.calculate_transport_cost()
            case 0:
                break
            case other:
                print("Sorry, this option does not exist!")

if __name__ == "__main__":
    menu()