from sqlalchemy import Table, Column, Integer, Boolean, ForeignKey, String, Date
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import ENUM, TINYINT, DATE

Base = declarative_base()

empl_proj = Table(
    "empl_proj",
    Base.metadata,
    Column("empl_id", Integer, ForeignKey("employee.id")),
    Column("proj_id", Integer, ForeignKey("project.id"))
)

class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    create_date = Column(Date)
    employees = relationship("Employee", backref=backref("department_backref"))

class Employee(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    surname = Column(String(50))
    login = Column(String(25))
    password = Column(String(50))
    email = Column(String(100))
    employee_role = Column(ENUM("Default", "PM", "Administrator"))
    salary = Column(Integer)
    department = Column(Integer, ForeignKey("department.id"))
    last_login_date = Column(Date)
    created_date = Column(Date)
    projects = relationship(
        "Project", secondary=empl_proj, back_populates="employees"
    )


class Project(Base):
    __tablename__ = "project"
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(String(255))
    project_status = Column(ENUM("Planned", "Ongoing", "Stopped"))
    created_status = Column(Boolean)
    start_date = Column(Date)
    stop_date = Column(Date)
    employees = relationship(
        "Employee", secondary=empl_proj, back_populates="projects"
    )
