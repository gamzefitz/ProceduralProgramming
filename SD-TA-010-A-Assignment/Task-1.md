Task 1 – Understanding Procedural Programming

What is a paradigm?

Programming paradigms are more about how the code is structured and less about which language is used. A programming language can support more than one paradigm. For example, a program written in Javascript can be purely procedural or purely object-oriented.

Some of the most common programming paradigms are Procedural, Object-oriented and Functional programming. Procedural programming is an imperative programming paradigm that involves implementing the behaviour of a program as procedures (or subroutines). Object-oriented, is another imperative programming paradigm but involves creating objects that contain both data structures and associated behaviours. Functional programming is a declarative programming paradigm in which functions are treated like any other data type, bound to identifiers,  passed as arguments and returned from other functions.

Core concepts of procedural programming

Top-down approach and sequential execution: Instructions are executed in a sequential order from top to bottom. Some languages allow importing/including libraries and similar resources. For example, in the C programming language, header files can be included in the beginning of the program. These files include pre-defined or user-defined procedures which help the programmer keep the source files tidy and easily readable. Control structures such as (for/while) loops and (if/switch) conditionals are used to manage the flow of the program.
Procedures and modularity: These are also known as functions or subroutines. They are blocks of code, each of which do a specific task and help break down a program into smaller and more manageable modules. These functions can be pre-defined and come with the language libraries. Alternatively, they can be user-defined where the programmer defines what the functions do as per the requirements of the program.
Passing parameters: Functions can take parameters allowing the program to perform operations with different data inputs, increasing the versatility and reusability of the code. The values passed as parameters can be passed by value or by reference. The actual values passed to the functions are called arguments. Parameters and arguments can often be used interchangeably.
Scoping: Local variables lifetime starts and ends within a function. Global variables are declared outside the functions and can be accessed from anywhere in the program. This means functions in one part of the program can change the value of the global variables, which in turn can impact the functionality in the other parts of the program.
Some of the programming languages that are predominantly suitable for procedural programming are Fortran, Algol, Cobol, Basic, Pascal and C.

Advantages

Structured approach encourages a clear and logical flow of code execution. It is easy to understand. Especially for beginners. 
Easy to test and debug. Modular design makes it easier to isolate and test individual parts of a program.
Performance for straightforward tasks. Procedural code produces efficient programs for specific tasks. It’s faster as there is no overhead for creating objects and memory can be directly manipulated.
Functions can be reused in different parts of the program. Especially, when executing batch tasks (such as in payroll transactions) the same routine can be executed as many times as needed.

Disadvantages

Hard to scale for big programs. When the programs get bigger and more complex, it’s more difficult to modify and extend the program or add/change features.
Less secure. There are no access modifiers. Data cannot be encapsulated or hidden from the rest of the program.
It’s not suitable to show the relationship between data and behaviour.
Code can become difficult to maintain as it grows. If the data structures change, many functions must also be changed.

Conclusion
Procedural programming is a good fit for Small to medium programs, scripting and automation, batch processing (such as payroll calculations), embedded systems and low level programming
