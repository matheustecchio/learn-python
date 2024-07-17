# Program Instructions
## Employee Workload:
- 7.5 hours/week on non-billable Comet product work.
- Up to 30 hours/week on billable project modifications for various customers (may be less than 30 hours).
- Up to 3 billable projects per day (may be less).

## Data Entry:
- Employees enter their 5-digit employee code and daily project information on Fridays.
- Each entry includes:
  - Project code (2 characters)
  - Number of hours worked (minimum unit: 30 minutes)
  - "ZZ" code for non-billable work (optional)


## Program Functionality:
**1. Data Input:**
- Prompt employee for their code.
- For each day (4 total):
  - Prompt employee for project code(s) and hours worked for each project.

**2. Daily Summary:**
- Display total hours worked for the day.

**3. Weekly Summary:**
- Display:
  - Total billable hours for the week.
  - Hours not worked on billable projects (in the 4 days).
  - Billable overtime hours (over 30 hours).
  - Average daily billable hours (rounded to 3 decimal places).
  - Project code with the most billed hours in a single day and the number of hours.

**4. Overtime Bonus (if applicable):**
- Calculate and display:
  - Number of overtime hours.
  - Overtime bonus (€20 per hour).

## Assumptions:
- Employees won't enter duplicate project entries for a single day.
- User data, except project hours, is assumed valid.

## Required Output:
- Design, code, and test a program to:
  - Read employee code and daily project data for each of the 4 days.
  - Display the weekly summary and overtime bonus information (if applicable).

- Formatting:
  - Averages displayed to 3 decimal places.
  - All other numeric values displayed to 2 decimal places.
  - Consistent and well-formatted output (spelling, capitalization).
## Description of Application

Your company has been contracted to produce the following program which a company makes available to its employees allowing them to calculate various charges. The charges are across the following 5 areas:

Tax, Monthly Pay (Sales), Water, Property Tax and School Transport

## Tax

Tax is calculated based on the user's salary less any tax-free allowance (TFA). The TFA is based on the number of children and monthly mortgage payments an individual has.

TFA:

- There is no allowance if the individual has no children.
- There is no allowance if the individual does not have a mortgage.
- There is no allowance if the monthly mortgage payment is less than €150.
- Where the number of children is 3 or fewer combined with monthly mortgage payments under €300 an allowance of €237 is available. For mortgage payments of €300 or more the allowance is €275.
- Where there are more than 3 children the allowance is €305

The tax rate is based on a person's total taxable income (salary less TFA) as follows:
- 20% on amounts up to €35,800 and 40% on the remainder.


## Monthly Pay for Sales Employees:

Most employees are on a fixed salary and so their monthly pay does not change. Only members of the sales team should have access to this functionality.

Monthly pay for sales staff is made up of a combination of basic pay (which can vary from employee to employee) and commission earned. The commission is based on the total value of the employee's

monthly sales, their number of years of service, their sales region (there are 6) and their mileage for the month.

For employees with 5 or more years of service working in one of the regions SW, MW, NW the commission rate is 4%. Where the mileage is over 2000 km, an extra 0.3% commission is awarded.

For employees in region SE, ME, NE the commission rate is 3%. Where the mileage is over 3000 km an extra 0.5% commission is awarded.

For employees with less than 5 years of service the original rate based on region is reduced by 0.5%. The remainder of the calculation is unchanged.

The total monthly pay is displayed followed by the total commission (nearest cent)

## Water Charges:

Water charges are paid yearly and calculated based on the total yearly household consumption (litres), the number of adults and the number of children in the house.
All households are allowed a basic usage of 213,000 litres/year. Charges are applied to volumes in excess of this amount at a rate of €3.70/litre. Certain allowances are available for large households as follows.

Households with 5 or more adults are allowed an extra 30,000 litres without charge. For such households, there is an extra allowance of 5000 litres/child for the 3rd and subsequent children.
Households with 3 or 4 adults are allowed an extra 20,000 litres along with 7,000 litres/child for the 3rd and subsequent children.

The charge (nearest cent). is displayed followed by the total allowances.

## Property Tax:

Property tax is calculated based on the property valuation, the location of the property and the monthly mortgage payment on the property. A number of allowances are available as follows

- 3 times the value of the monthly mortgage payment (if any).
- Since properties in Dublin are more expensive than elsewhere in the country there is an allowance of 15.4% of the value of the property for properties under €500,000 and 8.2% otherwise.

The tax due is calculated based on the property valuation, less any allowances, as follows:

- 0.2% for the first €300,000
- 0.25% for the next €200,000
- 0.3% for the next €500,000
- 0.35% on any amount over €1,000,000

The tax is displayed (nearest euro) followed by the total allowances (nearest cent).

## School Transport:

School transport is provided at a subsidised cost to school children who live more than a certain distance from the nearest school. In the case of primary-level students the minimum distance is 3.2 km, for second-level students the minimum distance is 4.8 km. Assume all first-level students are the
same distance from the school, and similarly for all second-level students. The cost per child is €100 for each of the first two primary-level students and €80 for each remaining primary-level student.
The cost is €350 for each of the first two second-level students and €300 for each remaining second- level student.

The amount any family must pay is capped as follows:

- For families with only primary-level students the amount due is capped at €390
- For families with only secondary-level students, or with some of each the amount is capped at €940

The amount due is displayed followed by the total saving (if any) due to the cost being capped. Both will be to the nearest euro.

## Notes:

- No global variables are to be used.
- The program should validate that all data entered is of the correct data type.
- All prompts and data output should be presented in a format that is easily understood by a novice user.
- The code will be modularised - i.e. functions will be used to break up the code into logical units.
