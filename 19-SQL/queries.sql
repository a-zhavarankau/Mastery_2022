""" 3.1 Get all employees full names from X departament """

SELECT CONCAT(employee.name, " ", employee.surname) AS Fullname FROM employee
WHERE department = (SELECT id FROM department WHERE name = "Java");

""" 3.2 How many employees in X departament """

SELECT COUNT(name) as Amount FROM employee
WHERE department = (SELECT id FROM department WHERE name = "Java");

""" 3.3 Get all employees which have Y project """

SELECT id, name from employee JOIN empl_proj
ON employee.id = empl_proj.empl_id WHERE proj_id = (SELECT id FROM project WHERE name = "GSA");

""" 3.4 Get all department names which are involved into project """

SELECT DISTINCT department.name FROM department JOIN employee
ON employee.department = department.id JOIN empl_proj
ON empl_proj.empl_id = employee.id WHERE empl_proj.proj_id=(SELECT id FROM project WHERE name = "GSA");

""" 3.5 Select all projects with total amount of employees salaries is bigger than 10k """

SELECT project.name FROM project JOIN empl_proj
ON empl_proj.proj_id = project.id JOIN employee
ON empl_proj.empl_id = employee.id GROUP BY project.name HAVING SUM(employee.salary) > 10000;

""" 3.6 Delete all department with 0 employees """

DELETE FROM department
WHERE NOT EXISTS (SELECT employee.name FROM employee WHERE employee.department = department.id);

