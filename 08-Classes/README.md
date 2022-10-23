# Classes

## Exercises  
Write your code in `company.py` file.

### 1. Create the following classes
#### 1.1 Class `Person`. It has 3 attributes - name, surname and private attribute age. Also add method instance method `who_are_you()`. It should print into the console the string “Hello, I am {name} {surname}” of the `Person`. Also this class should overload `__repr__` method.
#### 1.2 Class `Department`. It has 2 attributes - name and list of persons working at that department. Also add a method to add new employee - `add_employee()`, which accepts person as a parameter. When each person is added to the department they introduce themself by calling method `who_are_you()` which prints their information into the console. Departments should also support merging. When I sum two departments I get a new department with all employees from both original departments. When departments are merged the final name is gonna look like concatenation of the two original departments names. Department also overloads `__repr__` method which prints the department name and all the persons in the department.
#### 1.3 Class `ContractEmployee`. It inherits from `Person` and adds one more attribute - `contract_start_date`. Also it overrides the method `who_are_you` from Person class. In that method it first calls base class implementation and then prints the following string into the console - “My start time with the company is {contract_start_date}”. 

### 2. Create an organisation
With those 3 classes lets create the following example. We gonna create 4 `ContractEmployee` objects with names 
- Perry Benson with company since 2002-10-01
- Hale Loxley with company since 2020-01-13
- Stan Ruiz with company since 2012 -04-12
- Raven Hart with company since 2003-05–08

Originally we gonna create two Departments:
- Engineering
- Business Analysts  
In first one we gonna put Perry and Hale and in the second one we gonna put Stan and Raven. 
Then me gonna merge those 2 departments like so:
```
      new_department = engineering + business_analyst
```
In the end print the new department.

