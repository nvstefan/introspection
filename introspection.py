# Домашнее задание
# по теме "Интроспекция"

import inspect
from types import ModuleType
import sys

def introspection_info(obj):
    # Определение типа объекта
    obj_type = type(obj).__name__

    # Получение атрибута объекта по имени
    obj_module = getattr(obj, "__module__", None)

    # Путь к расположению файла
    module_path = sys.modules[obj_module].__file__ if obj_module in sys.modules else None

    # Получение атрибутов объекта
    attributes = dir(obj)

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Определение модуля, к которому объект принадлежит
    module = obj.__class__.__module__

    # Проверяем наличие документации у объекта
    docstring = getattr(obj, '__doc__', None)

    # Создание словаря с информацией об объекте
    info = {
        'type': obj_type,
        'obj_module': obj_module,
        'module_path': module_path,
        'attributes': attributes,
        'methods': methods,
        'module': module,
        'docstring': docstring,
    }
    return info

number_info = introspection_info(42)
print("Информация о числе:")
for key, value in number_info.items():
    print(f"{key}: {value}")

class MyClass:
    def __init__(self, number):
        self.number = number

    def method(self):
        pass

instance_info = introspection_info(MyClass(10))
print("\nИнформация об экземпляре класса:")
for key, value in instance_info.items():
    print(f"{key}: {value}")


