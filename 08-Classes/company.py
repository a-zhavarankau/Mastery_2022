class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.__age: int

    def who_are_you(self):
        print(f"Hello, I am {self.name} {self.surname}")

    def __repr__(self):
        print(f"Person is {self.name} {self.surname}")


class Department:
    def __init__(self, name: str, workers: list = None):
        self.name = name
        self.workers = workers or []

    def add_employee(self, person):
        self.workers.append(person)
        Person.who_are_you(person)

    def __print_workers(self):
        for i in self.workers:
            print(f"- {i.name} {i.surname}")

    def __repr__(self):
        print(f"Department {self.name!r} includes the next employees:")
        self.__print_workers()

    def __add__(self, other):
        name = self.name + other.name
        workers = self.workers[:]
        workers.extend(other.workers)
        return Department(name, workers)


class ContractEmployee(Person):
    def __init__(self, name, surname, contract_start_date: str = None):
        super().__init__(name, surname)
        self.name = name
        self.surname = surname
        self.contract_start_date = contract_start_date

    def who_are_you(self):
        super().who_are_you()
        print(f"My start time with the company is {self.contract_start_date}")


perry = ContractEmployee("Perry", "Benson", "2002-10-01")
hale = ContractEmployee("Hale", "Loxley", "2020-01-13")
stan = ContractEmployee("Stan", "Ruiz", "2012-04-12")
raven = ContractEmployee("Raven", "Hart", "2003-05–08")

engineering = Department("Engineering")
business_analyst = Department("Business Analysts")
engineering.add_employee(perry)
engineering.add_employee(hale)
business_analyst.add_employee(stan)
business_analyst.add_employee(raven)

new_department = engineering + business_analyst
new_department.__repr__()
