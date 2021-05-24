# Нужно создать класс который принимет модель ноутбука(Acer, Asus, ...) и возвращает полную комплектацию ноутбука со всеми характеристиками.
# В характеристики должны входить:
# Процессор
# Оперативная Память
# Видео карта
# Жёсткий Диск
# Материнская плата
# Размер экрана
# Для каждой характеристики создайте внутри класса функцию которая добавляет по одной характеристики к Dictionary.
# В итоге Ваш класс должен вернуть Dictionary в котором перечислены:
# Модель Ноутбука и его Характеристики


# class Notebook:
#     def __init__(self, model, cpu, ram, video, hdd, motherboard, screen):
#         self.model = model
#         self.cpu = cpu
#         self.ram = ram
#         self.video = video
#         self.hdd = hdd
#         self.motherboard = motherboard
#         self.screen = screen
#
#     def get_dict(self):
#         laptops = {'Модель ноутбука': [], 'Процессор': [], 'Оперативная память': [], 'Видекарта': [],
#                    'Жесткий диск': [], 'Материнская плата': [], 'Диогональ экрана': []}
#
#         laptops['Модель ноутбука'].append(self.model)
#         laptops['Процессор'].append(self.cpu)
#         laptops['Оперативная память'].append(self.ram)
#         laptops['Видекарта'].append(self.video)
#         laptops['Жесткий диск'].append(self.hdd)
#         laptops['Материнская плата'].append(self.motherboard)
#         laptops['Диогональ экрана'].append(self.screen)
#         print(laptops)
#
# model = Notebook('Acer', 'intel core i7', 'DDR4 16GB', 'Nvidia rtx 30', 'HDD 2048GB', 'Материнская плата hbr', 'Размер экрана 15,6 дюймов')
# model.get_dict()


# Нужно создать класс который принимает данные в формате dict. Эти данные, вы сможете взять из Data #1.
# Вам нужно создать 6 методов класса:
# Получить все ключи в TUPLE.
# Получить все значения в TUPLE.
# Получить все ключи в LIST.
# Получить все значения в LIST.
# Получить все ключи в SET.
# Получить все значения в SET.
# Ниже когда вы будете передавать Словарь классу он и вызывать из него любой метод Вы должны получать соответственно нужные типы данных.
# Example: my_class = Parser("DICT") | my_class.get_keys_tuple()

# class Class:
#     def __init__(self):



colors = {
    "black": {
        "category": "hue",
        "type": "primary",
        "code": {
            "rgba": [255, 255, 255, 1],
            "hex": "#000"
        }
    }}
#     "white": {
#         "category": "value",
#         "type": "primary",
#         "code": {
#             "rgba": [0, 0, 0, 1],
#             "hex": "#FFF"
#         }
#     },
#     "red": {
#         "category": "hue",
#         "type": "primary",
#         "code": {
#             "rgba": [255, 0, 0, 1],
#             "hex": "#FF0"
#         }
#     },
#     "blue": {
#         "category": "hue",
#         "type": "primary",
#         "code": {
#             "rgba": [0, 0, 255, 1],
#             "hex": "#00F"
#         }
#     },
#     "yellow": {
#         "category": "hue",
#         "type": "primary",
#         "code": {
#             "rgba": [255, 255, 0, 1],
#             "hex": "#FF0"
#         }
#     },
#     "green": {
#         "category": "hue",
#         "type": "secondary",
#         "code": {
#             "rgba": [0, 255, 0, 1],
#             "hex": "#0F0"
#         }
#     }
# }

tuples = tuple()
key = colors.keys()
print(key)
tuples.append(key)
print(tuples)

