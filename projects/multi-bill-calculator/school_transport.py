def calculate_transport_cost():

    MIN_DISTANCE_PRIMARY = 3.2  # Minimum distance for primary-level students in kilometers
    MIN_DISTANCE_SECONDARY = 4.8  # Minimum distance for second-level students in kilometers
    COST_FIRST_TWO_PRIMARY = 100  # Cost per child for the first two primary-level students
    COST_REMAINING_PRIMARY = 80  # Cost per child for remaining primary-level students
    COST_FIRST_TWO_SECONDARY = 350  # Cost per child for the first two second-level students
    COST_REMAINING_SECONDARY = 300  # Cost per child for remaining second-level students
    PRIMARY_FAMILY_CAP = 390  # Maximum amount due for families with only primary-level students
    SECONDARY_FAMILY_CAP = 940  # Maximum amount due for families with only secondary-level students

    # Take input from the user for the number of primary-level and second-level students
    print("--Welcome To The School Transport Calculator--")
    primary_students = int(input("Enter the number of primary-level students: "))
    secondary_students = int(input("Enter the number of second-level students: "))

    total_cost = 0

    # Calculate total distance for primary-level students
    total_distance_primary = primary_students * MIN_DISTANCE_PRIMARY

    # Calculate total distance for second-level students
    total_distance_secondary = secondary_students * MIN_DISTANCE_SECONDARY

    # Calculate cost for primary-level students
    if primary_students <= 2:
        total_cost += primary_students * COST_FIRST_TWO_PRIMARY
    else:
        total_cost += 2 * COST_FIRST_TWO_PRIMARY
        total_cost += (primary_students - 2) * COST_REMAINING_PRIMARY

    # Calculate cost for second-level students
    if secondary_students <= 2:
        total_cost += secondary_students * COST_FIRST_TWO_SECONDARY
    else:
        total_cost += 2 * COST_FIRST_TWO_SECONDARY
        total_cost += (secondary_students - 2) * COST_REMAINING_SECONDARY

    # Apply family caps
    if primary_students > 0 and secondary_students == 0:
        total_cost = min(total_cost, PRIMARY_FAMILY_CAP)
    elif secondary_students > 0 and primary_students == 0:
        total_cost = min(total_cost, SECONDARY_FAMILY_CAP)
    else:
        total_cost = min(total_cost, max(PRIMARY_FAMILY_CAP, SECONDARY_FAMILY_CAP))

    # Print the total cost
    print("Total cost for providing subsidized transport: {} euro".format(total_cost))

if __name__ == "__main__":
    calculate_transport_cost()
