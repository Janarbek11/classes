# 1. Создайте класс Factory и внутри создайте 2 метода:
    # Метод engine который возвращает строку "Двигатель создан"
    # Метод bridge который возвращает строку "Ходовая часть создана"


# class Factory:
#     def engine(self):
#         return 'Двигатель создан!'
#
#     def bridge(self):
#         return 'Ходовая часть создана!'
#
#
# cl = Factory()
# print(cl.engine())
# print(cl.bridge())


# 2. Создайте класс Toyota который будет НАСЛЕДОВАТЬ класс Factory. В классе Toyota создайте методы wheels и windows.
    # Метод wheels возвращает строку "Колёса готовы"
    # Метод windows возвращает строку "Стёкла готовы"
    # Из класса Toyota вызовите все методы, методы вернут вам строки(объекты)
    # Результат каждого метода вставьте в лист


# class Toyota(Factory):
#     def wheels(self):
#         return 'Колёса готовы!'
#
#     def window(self):
#         return 'Стёкла готовы!'
#
#
# a = []
# t = Toyota()
# a.append(t.engine())
# a.append(t.bridge())
# a.append(t.wheels())
# a.append(t.window())
# print(a)


# Создайте Класс Zoo.
# Инициализируйте класс в объект.
# К объекту Zoo добавьте атрибут animal_1 и присвойте ему значение "Тигр"
# К объекту Zoo добавьте атрибут animal_2 и присвойте ему значение "Бегемот"
# К объекту Zoo добавьте атрибут animal_3 и присвойте ему значение "Жираф"
# В объекте Zoo измените значение атрибута animal_1 и присвойте ему значение "Лев".
# К объекту Zoo добавьте атрибут animal_4 и присвойте ему list состоящий из animal_2 и animal_3
# В объекте Zoo измените значение атрибута animal_3 и присвойте ему значение "Змея".


# class Zoo:
#     def __init__(self):
#         self.animal1 = "Тигр"
#         self.animal2 = "Бегемот"
#         self.animal3 = "Жираф"
#
#
# z = Zoo()
# z.animal1 = "Лев"
# z.animal4 = [z.animal2, z.animal3]
# z.animal3 = "Змея"
# print(z.animal1, z.animal2, z.animal3, z.animal4)

# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
# department, year_of_entrance. Добавьте метод get_student_info, который
# возвращает имя, фамилию, год поступления и факультет в
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
# Программирование.”


# class Student:
#     def __init__(self, name, last_name, department, year_of_entrance):
#         self.name = name
#         self.last_name = last_name
#         self.department = department
#         self.year_of_entrance = year_of_entrance
#
#     def get_student_info(self):
#         return f'{self.name, self.last_name} поступил в {self.year_of_entrance}г на факультет: {self.department}'
#
# st = Student('Janarbek', 'Keneshbekov', 'Программирование', 2018)
# print(st.get_student_info())


# 2)Airplane
# Создайте новый класс Airplane. Создайте следующие характеристики (полей)
# объекта:
# ● make (марка)
# ● model
# ● year
# ● max_speed
# ● odometer
# ● is_flying
# и методы имитирующих поведение самолета take off (взлет), fly (летать), land
# приземление). Метод take off должен изменить is_flying на True, а land на False. По
# умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
# изменять показания одометра (километраж). Создайте 1 объект класса и используйте
# все методы класса.

# class Airplane:
#     def __init__(self, make, model, year, max_speed, odometer, is_flying):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.max_speed = max_speed
#         self.odometer = odometer
#         self.is_flying = is_flying
#
#     def take_off(self):
#         self.is_flying = True
#         return self.is_flying
#
#     def fly(self, value):
#         self.odometer += value
#         return self.odometer
#
#     def land(self):
#         self.is_flying = False
#         return self.is_flying
#
#
# air = Airplane('BOEING 777', 'zvezda', 1994, '965 км/ч', '6 831 км', True)
#
# print(air.take_off())
# print(air.fly('519 км/ч'))
# print(air.land())


# class Airplane:
#
#     def init(self, make, model, year, max_speed, odometr, is_flying = False):
#
#        self.make = make
#        self.model = model
#        self.year = year
#        self.max_speed = max_speed
#        self.odometr = odometr
#        self.is_flying = is_flying
#
#     def take_off(self):
#         self.is_flying = True
#         print('Взлет')
#
#     def fly(self):
#         self.odometr = int(input('Введите расстояние полета: '))
#         print('Полет нормальный')
#         print(self.odometr, 'км')
#
#     def land(self):
#         self.is_flying = False
#         print('Приземление')
#
#
# a = Airplane()
# a.take_off()
# print(a.is_flying)
# a.fly()
# a.land()
# print(a.is_flying)

# 3)Car
# Создайте класс Car. Пропишите в конструкторе параметры make, model, year,
# odometer, fuel. Пусть у показателя odometer будет первоначальное значение 0,
# а у fuel 70. Добавьте метод drive, который будет принимать расстояние в км. В
# самом начале проверьте, хватит ли вам бензина из расчета того, что машина
# расходует 10 л / 100 км (1л - 10 км) . Если его хватит на введенное расстояние,
# то пусть этот метод добавляет эти километры к значению одометра, но не
# напрямую, а с помощью приватного метода __add_distance. Помимо этого
# пусть метод drive также отнимет потраченное количество бензина с помощью
# приватного метода __subtract_fuel, затем пусть распечатает на экран “Let’s
# drive!”. Если же бензина не хватит, то распечатайте “Need more fuel, please, fill
# more!”

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.fuel = 70
#         self.spidometr = 0
#
#     def drive(self):
#         distance = int(input('Введите расстояние: '))
#         fuel = distance / 10
#         if fuel > self.fuel:
#             print('Need more fuel!')
#             return self.spidometr
#         if fuel <= self.fuel:
#             self.spidometr += distance
#             self.fuel -= fuel
#             print("Let's drive")
#             return self.spidometr, self.fuel
#
#     def __add_distance(self):
#         pass
#
#     def __subtract_fuel(self):
#         pass
#
# a = Car('Toyota', 'Supra', 2004)
# print(a.drive())
# print(a.drive())


# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.

# class ContactList(list):
#
#     def search_by_name(self, name):
#         all_contacts = []
#         for i in self:
#             if name in i:
#                 all_contacts.append(i)
#         return all_contacts
#
#
# contacts = ContactList()
# contacts.append('Janar')
# contacts.append('Janar')
# contacts.append('Aibek')
# contacts.append('Atai')
# contacts.append('Mirbek')
# print(contacts)
# print(contacts.search_by_name('Janar'))

class Soldier:
    def __init__(self, name):
        self.name = name

class Guns:
    def __init__(self):
        self.num = 50

    def ak47(self, name):
        for i in range(self.num):
            print(f'Солдлат {self.name.title()}, кричит tigi-tigitishh!\n')
            if self.num:
                count = 0
                for x in range(self.num):
                    count += 1
                    self.num -= 1
                    print("\t\t\tti-gi-ti-gi-tish", count)



