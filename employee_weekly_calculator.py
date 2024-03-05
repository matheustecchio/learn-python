def main():
    """
    This function calculates and displays weekly work summary for an employee.
    """

    # Get employee code from user
    employee_code = input("\nEnter employee code (5 digits): ")

    total_billable_hours = 0
    total_non_billable_hours = 7.5 # Fixed non-billable hours
    total_overtime_hours = 0
    total_days = 4 # Fixed number of workdays
    max_project_hours = 0
    max_project_code = ""

    # Iterate through each day
    for day in range(total_days):
        print(f"\nDay {day + 1}:")
        daily_total_hours = 0

        # Input hours for up to 3 projects per day
        for i in range(3):
            project_code = input("Enter project code (or 'ZZ' to leave ): ").upper()
            if project_code == 'ZZ':
                break

            # Get and validate project hours
            hours = float(input("Enter hours worked on the project: "))
            daily_total_hours += hours
            total_billable_hours += hours
            if hours > max_project_hours:
                max_project_hours = hours
                max_project_code = project_code

    # Calculate overtime and bonus
    overtime_hours = total_billable_hours - 30
    if overtime_hours > 0:
        payable_overtime_hours = overtime_hours * 20
    else:
        overtime_hours = 0

    # Display results
    print("\nWeekly Summary:")
    print(f"Total Billable Hours: {total_billable_hours:.2f} hours")
    print(f"Non-Billable Hours: {total_non_billable_hours:.2f} hours")
    print(f"Billable Overtime Hours: {overtime_hours:.2f} hours")
    print(f"Average Billable Daily Hours: {total_billable_hours / total_days:.3f} hours")
    print(f"Project with Most Hours: Project Code: {max_project_code} - {max_project_hours:.2f} hours\n")


    if overtime_hours > 0:
        print(f"Overtime Bonus: €{payable_overtime_hours:.2f}\n")


if __name__ == "__main__":
    main()

