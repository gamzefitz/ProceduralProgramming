## Task 4 – Maintaining, Supporting, and Testing a Procedural Programming Application

### 1. Introduction
The payroll processing application was tested manually by running the program many times and entering different inputs every time in different scenarios and observe the result in terminal. The aim of this testing was to ensure the system handles undesired user inputs and guides the user where necessary as well as checking that each screen produces what is required in the design stage.

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
|T05|Employee ID format|Invalid|ab1|error:
|T06|Employee ID exists|Invalid|id999|error:
|T07|Menu option|Invalid|5|error:
|T08|Menu option|Invalid|a|error:
|T09|Menu option|Invalid|empty|error:
|T10|Salary data|Invalid|asd|error:
|T11|Salary data|Boundary|10000
|T12|PPSN format|Invalid|123456a|
|T13|PPSN exists|Invalid|1234567a|

##### Testing add/remove/edit employee
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T14|Add employee|Normal|jane doe, it, developer, 35000, 9876543z|employee added
|T15|Add another employee|Normal|john doe, it, developer, 35000, 8976543z|employee added
|T16|Change mind before removing employee|Normal|select n|returns to profile
|T17|Remove employee|Normal|select y|record deleted
|T18|Change mind before editing salary|Normal|select c|profile remains unchanged
|T19|Edit salary|Normal|enter 54090|salary updated

##### Testing display payslip/profile
|Test ID|Feature|Input Type|Input|Expected Output|Actual Output|Pass/Fail|
|---|---|---|---|---|---|---|
|T20|Display payslip|Normal|select display payslip|payslip displays in correct format and correct data
|T21|Display profile|Normal|enter ID|correct profile shows with full details

### 3. Recommendations

### 4. Supporting Documentation