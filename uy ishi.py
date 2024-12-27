# 1
# from dataclasses import dataclass
#
# @dataclass
# class Product:
#     name: str
#     _price: float
#     available: bool
#
#     @property
#     def price(self):
#         return self._price
#
#     @price.setter
#     def price(self, value):
#         if value > 0:
#             self._price = value
#         else:
#             raise ValueError("Narx faqat ijobiy bo'lishi kerak!")
#
#
# class ElectronicProduct(Product):
#     warranty_period: int
#
#     def __init__(self, name, price, available, warranty_period):
#         super().__init__(name, price, available)
#         self.warranty_period = warranty_period
#
# product = Product(name="Telefon", _price=3000, available=True)
# print(f"Mahsulot: {product.name}, Narx: {product.price}, Mavjudligi: {product.available}")
#
# try:
#     product.price = 3500
#     print(f"Yangilangan narx: {product.price}")
# except ValueError as e:
#     print(e)
#
# electronic = ElectronicProduct(name="Kompyuter", price=10000, available=True, warranty_period=24)
# print(f"{electronic.name} kafolat muddati: {electronic.warranty_period} oy, Narxi: {electronic.price}")

# -----------------------------------------------
# 2
# from dataclasses import dataclass
#
# @dataclass
# class Vehicle:
#     brand: str
#     _speed: int
#
#     @property
#     def speed(self):
#         return self._speed
#
#     @speed.setter
#     def speed(self, value):
#         if value <= 300:
#             self._speed = value
#         else:
#             raise ValueError("Tezlikni 300 dan oshirib bo'lmaydi!")
#
#
# class Car(Vehicle):
#     fuel_type: str
#
#     def __init__(self, brand, speed, fuel_type):
#         super().__init__(brand, speed)
#         self.fuel_type = fuel_type
#
#
# class Bicycle(Vehicle):
#     brake_type: str
#
#     def __init__(self, brand, speed, brake_type):
#         super().__init__(brand, speed)
#         self.brake_type = brake_type
#
# car = Car(brand="Tesla", speed=250, fuel_type="Elektr")
# print(f"Transport vositasi: {car.brand}, Tezligi: {car.speed} km/h, Yoqilg'i turi: {car.fuel_type}")
#
# try:
#     car.speed = 320
# except ValueError as e:
#     print(e)
#
# bicycle = Bicycle(brand="Shimano", speed=25, brake_type="Disk")
# print(f"Velosiped: {bicycle.brand}, Tezligi: {bicycle.speed} km/h, Tormoz turi: {bicycle.brake_type}")

# ----------------------------------------------------------------
# 3
# from dataclasses import dataclass
#
# @dataclass
# class Book:
#     title: str
#     author: str
#     _price: float
#
#     def update_price(self, value, is_admin):
#         if is_admin:
#             self._price = value
#         else:
#             raise PermissionError("Faqat admin narxni o'zgartirishi mumkin!")
#
#
# class EBook(Book):
#     file_size: float
#
#     def __init__(self, title, author, price, file_size):
#         super().__init__(title, author, price)
#         self.file_size = file_size
#
#
# class PrintedBook(Book):
#     paper_type: str
#
#     def __init__(self, title, author, price, paper_type):
#         super().__init__(title, author, price)
#         self.paper_type = paper_type
#
# ebook = EBook(title="Python dasturlash", author="John Smith", price=15.0, file_size=2.5)
# print(f"E-kitob: {ebook.title}, Muallif: {ebook.author}, Fayl hajmi: {ebook.file_size} MB, Narxi: ${ebook._price}")
#
# try:
#     ebook.update_price(12.0, is_admin=True)
#     print(f"Yangilangan narx (admin): ${ebook._price}")
# except PermissionError as e:
#     print(e)
#
# printed_book = PrintedBook(title="Matematika asoslari", author="Jane Doe", price=20.0, paper_type="Glossy")
# print(f"Qog'oz kitob: {printed_book.title}, Muallif: {printed_book.author}, Qog'oz turi: {printed_book.paper_type}")

# ------------------------------------------------------
# 4
# from dataclasses import dataclass
#
# @dataclass
# class Employee:
#     name: str
#     position: str
#     _salary: float
#
#     def raise_salary(self, amount, is_director):
#         if is_director:
#             self._salary += amount
#         else:
#             raise PermissionError("Faqat direktor maoshni oshirishi mumkin!")
#
#
# class Manager(Employee):
#     def manage_team(self):
#         return f"{self.name} jamoani boshqarish vazifasini bajaradi."
#
#
# class Developer(Employee):
#     def write_code(self):
#         return f"{self.name} kod yozmoqda."
#
# manager = Manager(name="Ali", position="Manager", _salary=5000)
# developer = Developer(name="Vali", position="Developer", _salary=4000)
#
# print(f"Ishchi: {manager.name}, Lavozim: {manager.position}, Maosh: ${manager._salary}")
# print(f"Ishchi: {developer.name}, Lavozim: {developer.position}, Maosh: ${developer._salary}")
#
# try:
#     manager.raise_salary(500, is_director=True)
#     print(f"Yangilangan manager maoshi: ${manager._salary}")
#     developer.raise_salary(500, is_director=False)
# except PermissionError as e:
#     print(f"Xatolik: {e}")

# -------------------------------------------------------
# 5
# from dataclasses import dataclass
#
# @dataclass
# class Athlete:
#     name: str
#     sport_type: str
#     _record: float
#
#     def update_record(self, new_record):
#         if new_record < self._record:
#             self._record = new_record
#         else:
#             raise ValueError("Yangi rekord avvalgisidan pastroq bo'lishi kerak!")
#
#
# class Runner(Athlete):
#     def run_distance(self, distance):
#         return f"{self.name} {distance}km masofani yuguradi."
#
#
# class Swimmer(Athlete):
#     def swim_pool(self, laps):
#         return f"{self.name} hovuzda {laps} aylanish suzadi."
#
# runner = Runner(name="Usain Bolt", sport_type="Yugurish", _record=9.58)
# swimmer = Swimmer(name="Michael Phelps", sport_type="Suzish", _record=1.54)
#
# print(f"Sportchi: {runner.name}, Sport turi: {runner.sport_type}, Rekord: {runner._record} soniya")
# print(f"Sportchi: {swimmer.name}, Sport turi: {swimmer.sport_type}, Rekord: {swimmer._record} daqiqa")
#
# try:
#     runner.update_record(new_record=9.50)
#     print(f"Yangilangan rekord: {runner._record} soniya")
# except ValueError as e:
#     print(f"Xatolik: {e}")
#
# print(runner.run_distance(100))
# print(swimmer.swim_pool(20))