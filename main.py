# from dataclasses import dataclass, field
# from typing import Any

# @dataclass
# class Person:
#     name: str
#     lastname: str
#     age: int
# p1 = Person("Sobir", "Sobirov",

# -----------------------------
# @dataclass
# class PersonData:
#     name: str
#     lastname: str
#     age: int = field(default=18, compare=False)
#     interests: list = field(default_factory=list)
#     info: str = field(init=False, compare=False)
#
#     def __post_init__(self):
#         self.info = f"Perdon: {self.name} {self.lastname} {self.age}"
#
# pd1 = PersonData("Sobir", "Sobirov", 58)
# pd2 = PersonData("Sobir", "Sobirov", 27)
# print(pd1)
# print(pd2)

# class Days:
#     @staticmethod
#     def my_days():
#         return ["Du", "Se", "Ch", "Pa", "Ju"]
#
#
# @dataclass
# class PersonData:
#     current_id = 0
#     id: int = field(init=False)
#     name: str
#     lastname: str
#     age: Any
#
#     def __post_init__(self):
#         PersonData.current_id += 1
#         self.id = PersonData.current_id
#
# @dataclass
# class Employee(PersonData):
#     age: int
#     salary: int
#     passport: str
#     work_days: list = field(default_factory=Days.my_days)
#
#     def __post_init__(self):
#         super().__post_init__()
#         print("Emoliyee ichida chiqarildi!!!")

