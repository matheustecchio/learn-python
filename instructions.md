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
