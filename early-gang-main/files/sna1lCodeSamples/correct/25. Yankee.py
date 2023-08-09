import asyncio
import array as arr
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    age: int

employees = [
    Employee("John", 25),
    Employee("Alice", 30),
    Employee("Bob", 28),
]

async def process_employees():
    for employee in employees:
        await asyncio.sleep(1)
        print(f"Processing employee: {employee.name}")
        if employee.age > 30:
            print(f"{employee.name} is above 30 years old!")

asyncio.run(process_employees())
