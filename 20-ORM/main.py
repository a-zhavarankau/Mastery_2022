import pymysql
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import asc, desc, func, distinct
from models import Department, Employee, Project
from config import user, password, host, db_name


url = f'mysql+pymysql://{user}:{password}@{host}/{db_name}'
engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()


# 3.1 Get all employees full names from X departament
def get_employees_names_from_department(session, dep_name: str):
    query_employees_names_from_department = (
        session
        .query((Employee.name + " " + Employee.surname).label("fullname"))
        .join(Department)
        .filter(Department.name == dep_name)
    )
    return query_employees_names_from_department


employees_names_from_department = \
    get_employees_names_from_department(session, dep_name="Python")
for employee in employees_names_from_department:
    print(employee)


# 3.2 How many employees in X departament
def get_employees_in_department(session, dep_name: str) -> list[tuple]:
    query_employees_in_department = (
        session
        .query(func.count(Employee.name).label("Amount"))
        .join(Department)
        .filter(Department.name == dep_name)
        .all()
    )
    return query_employees_in_department


employees_in_department = \
    get_employees_in_department(session, dep_name="Java")
print(employees_in_department)


# 3.3 Get all employees which have Y project
def get_employees_from_project(session, proj_name: str):
    query_employees_from_project = (
        session
        .query(Employee.name)
        .join(Project.employees)
        .filter(Project.name == proj_name)
    )
    return query_employees_from_project


employees_from_project = \
    get_employees_from_project(session, proj_name="GSA")
for employee in employees_from_project:
    print(employee)


# 3.4 Get all department names which are involved into project
def get_departments_from_project(session, proj_name: str):
    query_departments_from_project = (
        session
        .query(distinct(Department.name))
        .join(Employee)
        .join(Employee.projects)
        .filter(Project.name == proj_name)
    )
    return query_departments_from_project


departments_from_project = \
    get_departments_from_project(session, proj_name="GSA")
for department in departments_from_project:
    print(department)


# 3.5 Select all projects with total amount of employees salaries is
#     bigger than 10k
def get_projects_defined_total_salary(session, total_sal):
    query_projects_defined_total_salary=(
        session
        .query(Project.name)
        .join(Employee.projects)
        .group_by(Project.name)
        .having(func.sum(Employee.salary) > total_sal)
    )
    return query_projects_defined_total_salary


projects_defined_total_salary = \
    get_projects_defined_total_salary(session, total_sal=10000)
for project in projects_defined_total_salary:
    print(project)


# 3.6 Delete all department with 0 employees
def delete_empty_departments(session):
    subq = (
        session
        .query(distinct(Employee.department))
    )
    query_empty_departments = (
        session
        .query(Department)
        .filter(Department.id.not_in(subq))
    )

    for department in query_empty_departments:
        session.delete(department)
    session.commit()
    return query_empty_departments


empty_departments = delete_empty_departments(session)
for department in empty_departments:
    print(department.id, department.name)
