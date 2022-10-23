# Clean code

The `report_creater` class holds the main functionality. It's `__init__` method receives a format of created report, for now it's `json` and `csv`.
In order to create report, call `create_report` method and pass a list of users.
`report_creater` saves result in the file named `output.` + format extension.

## Exercises

1. Refactor `report_creater` class in `report.py`:
1.2 The code must follow PEP code standards.
1.3 Add type hints for methods.
1.4 The code must follow DRY, KISS and SOLID principles.
1.5 You can freely rename class and all methods, parameters or variables.
1.6 You can create new classes if needed.
1.7 The output of the class must remain the same.
1.8 The final class must be easily extended with new output formats if needed.
