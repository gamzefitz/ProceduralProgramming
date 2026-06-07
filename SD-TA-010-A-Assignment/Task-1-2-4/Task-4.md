## Task 4 – Maintaining, Supporting, and Testing a Procedural Programming Application

### 1. Introduction
The payroll processing application was tested manually by running the program many times and entering different inputs across different scenarios and observing the results in the terminal.

The aim of this testing was to ensure the system handles undesired user inputs and guides the user where necessary, ensuring that each screen produces what is required in the design stage.

### 2. Test Table

##### Testing payslip calculations
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T01|Monthly gross|Normal|54000|4500.00|4500.00|Pass|
|T02|Monthly PAYE|Boundary|44000|420.83|420.83|Pass|
|T03|Monthly USC|Boundary|13000|0.00|0.00|Pass|
|T04|Monthly PRSI|Boundary|18304|0.00|0.00|Pass|

##### Testing input validations
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T05|Employee ID format|Invalid|ab1|Invalid input message: Not a valid ID. Try again or press (c) to cancel.| Same as expected|Pass|
|T06|Employee ID exists|Invalid|id999|ID error message: This ID does not exist. Try again or press (c) to cancel.|Same as expected|Pass|
|T07|Menu option|Invalid|5|Invalid input message: Invalid input. Press 1, 2, 3 or 4...|Same as expected|Pass|
|T08|Press enter to go back|Normal|Enter|Returns to profile|Program ended abruptly|Fail|
|T09|Name too long|Invalid|Bartholomew Vanderburg|Input too long error: Name is too long. Enter 20 characters or less:|Same as expected|Pass|
|T10|Salary data|Invalid|asd|Invalid input error: Invalid input. Press (c) to cancel or enter a valid salary amount. Salary can only be numeric and 5 or 6 digits|Validation works correctly but the error message has copy paste error: Role is too long. Enter 20 characters or less|Fail|
|T11|Salary data|Boundary|10000|Salary detail is updated|Same as expected|Pass|
|T12|PPSN format|Invalid|123456a|Invalid input message: Enter a valid PPSN:|Same as expected|Pass|
|T13|PPSN exists|Invalid|1234567a|PPSN error message: This PPS number is already in the system.|Same as expected|Pass|

##### Testing add/remove/edit employee
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T14|Add employee|Normal|jane doe, it, developer, 35000, 9876543z|Record added|Same as expected|Pass|
|T15|Add another employee|Normal|john doe, it, developer, 35000, 8976543z|Record added|Same as expected|Pass|
|T16|Change mind before removing employee|Normal|Select n|Returns to profile|Same as expected|Pass|
|T17|Remove employee|Normal|Select y|Record deleted|Same as expected|Pass|
|T18|Change mind before editing salary|Normal|Select c|Profile remains unchanged|Same as expected|Pass|
|T19|Edit salary|Normal|Enter 54090|Salary updated|Same as expected|Pass|

##### Testing display payslip/profile
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T20|Display payslip|Normal|Select display payslip|Payslip displays in correct format and correct data|Same as expected|Pass|
|T21|Display profile|Normal|Enter ID1|Alice Murphy's profile shows with full details|Same as expected|Pass|

### 3. Recommendations

These improvements are suggested for the program:
- The Help menu needs to be expanded. Currently, there is a placeholder for the Help content. The content can be organized under titles for each menu, explaining what each option does.
- The requirements state that this application should support up to 50 employees but there is no enforcement in the source code to limit the number of employee records stored in employees.json.
- There is an input validation function checking the salary input format. However, there is no validation that checks realistic amounts or minimum wage amount. As a result, a user can add a very low annual salary (e.g. €10000) for an employee and the system will accept it without any warning.
- There is an input validation function checking the user inputs in the Add New Employee screen. Currently, these validations enforce a limit of 20 characters. This may not be realistic for some names where the last name is really long or when the employee has more than one name (e.g. a middle name).
- It would be a better idea to select department and role from a pre-set list of departments and roles when adding a new employee. This would avoid inconsistent data input such as "IT" and "Information Technologies" which actually point to the same department.
- Currently, there is no way to go back to a previous menu in the Add New Employee screen without adding the details in the correct format. If a user changes their mind and wants to cancel filling in the new employee form, they have no option but to enter dummy info, save it in the system and then go back to remove the same record from the system.

### 4. Supporting Documentation

**User Guide**
- To run the program:
    1. Ensure Python 3.12 or higher is installed on the machine.
    2. Ensure all of the source files, including the employees.json, are in the same directory.
    3. Click the Play button at the top of the file in Visual Studio Code. Alternatively, you can start the program from the terminal by typing `python3 payroll_program.py` in the directory where the source file is.
- Menu options accept appropriate keyboard inputs followed by pressing Enter.
- Viewing the output in a large monitor is recommended for a better experience. Smaller screens introduce the risk of terminal output being wrapped.

**Code Documentation**
- **payroll_program.py:** This is where the program starts. It imports payslip_calculations and input_validations. All screen functions are contained in this file.

- **payslip_calculations.py:** This file includes all the functions to make salary and tax calculations.

- **input_validations.py:** User input validations are handled by the functions in this file.

**Assumptions/Requirements**

- This application should be run with a Python version of 3.12 or higher. Older versions do not support single quotes in f-strings which this program relies on to run smoothly.

- The formatting of the payslip and the employee profiles were designed with small laptop screens in mind. However, if the terminal screen is too small, the formatting might not look as designed, some lines may be wrapped or truncated.