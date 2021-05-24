class Human:
    # Статические поля, атрибуты
    default_name = 'No name'
    default_age = '0'

    def init(self, name=default_name, age=default_age):
        # Динамические поля
        # Публичные
        self.name = name
        self.age = age

        # Приватные
        self.money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.__money}")
        print(f"House: {self.__house}")

    # Статический метод
    @staticmethod
    def default_info():
        print(f"Default name: {Human.default_name}")
        print(f"Default age: {Human.default_age}")

    def earn_money(self, amount):
        self.__money += amount
        print(f"Erned {amount} money! Current value: {self.__money}")

    def buy_house(self, house, discont):
        price = house.final_price(discont)
        if self.__money >= price:
            self.__make_deal(house, price)

    # Приватный метод
    def __make_deal(self, house, price):
        self.__money = price
        self.__house = house


class House:
    def __init(self, _area, price):
        self._area = _area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f"Final price: {final_price}")
        return final_price

class SmallHouse:
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area)
#
# if name == "main":
#     nurbek = Human("Janarbek", 20)
#     nurbek.info()
#     nurbek.default_info()
#     nurbek.earn_money(10000)

jake = Human.default_info()

SmallHouse()

# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.


