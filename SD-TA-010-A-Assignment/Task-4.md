## Task 4 – Maintaining, Supporting, and Testing a Procedural Programming Application

### 1. Introduction
The payroll processing application was tested manually by running the program many times and entering different inputs across different scenarios and observing the results in the terminal. The aim of this testing was to ensure the system handles undesired user inputs and guides the user where necessary as well as checking that each screen produces what is required in the design stage.

### 2. Test Table

##### Testing payslip calculations
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T01|Monthly gross|Normal|54000|4500.00|
|T02|Monthly PAYE|Boundary|44000|420.83|
|T03|Monthly USC|Boundary|13000|0.00|
|T04|Monthly PRSI|Boundary|18304|0.00|

##### Testing input validations
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T05|Employee ID format|Invalid|ab1|error:|
|T06|Employee ID exists|Invalid|id999|error:|
|T07|Menu option|Invalid|5|error:|
|T08|Menu option|Invalid|a|error:|
|T09|Menu option|Invalid|empty|error:|
|T10|Salary data|Invalid|asd|error:|
|T11|Salary data|Boundary|10000|
|T12|PPSN format|Invalid|123456a|
|T13|PPSN exists|Invalid|1234567a|

##### Testing add/remove/edit employee
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T14|Add employee|Normal|jane doe, it, developer, 35000, 9876543z|employee added|
|T15|Add another employee|Normal|john doe, it, developer, 35000, 8976543z|employee added|
|T16|Change mind before removing employee|Normal|select n|returns to profile|
|T17|Remove employee|Normal|select y|record deleted|
|T18|Change mind before editing salary|Normal|select c|profile remains unchanged|
|T19|Edit salary|Normal|enter 54090|salary updated|

##### Testing display payslip/profile
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T20|Display payslip|Normal|select display payslip|payslip displays in correct format and correct data|
|T21|Display profile|Normal|enter ID|correct profile shows with full details|

### 3. Recommendations

These improvements are suggested for the application:
- Help menu needs to be expanded. Currently, there is a placeholder for the Help content. The content can be organized under titles for each menu, explaining what each option does.
- Requirements state that this application should support up to 50 employees but there is no enforcement in the source code to limit the number of employee records stored in employees.json.
- There is an input validation function checking the salary input format. However, there is no validation that checks realistic amounts or minimum wage amount. As a result, a user can add a very low annual salary (e.g. €10000) for an employee and it can go unnoticed.
- There is an input validation function checking the user inputs in Add New Employee screen. Currently, these validations enforce a limit of 20 characters. This may not be realistic for some names where the last name is really long or when the employee has more than one name (e.g. a middle name).
- It would be a better idea to select department and role from a pre-set list of departments and roles when adding a new employee. This would avoid inconsistent data input such as "IT" and "Information Technologies" which actually point to the same department. 

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