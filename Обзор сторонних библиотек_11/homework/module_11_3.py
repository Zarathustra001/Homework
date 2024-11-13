import inspect


def introspection_info(obj):
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Модуль (если есть)
    module = inspect.getmodule(obj)
    info['module'] = module.__name__ if module else None

    # Атрибуты
    attributes = []
    for name in dir(obj):
        if not name.startswith('__'):  # Игнорируем "магические" атрибуты
            value = getattr(obj, name)
            attributes.append({'name': name, 'value': value, 'type': type(value).__name__})
    info['attributes'] = attributes

    # Методы (callable атрибуты)
    methods = []
    for name in dir(obj):
        if not name.startswith('__'):
            value = getattr(obj, name)
            if callable(value):
                methods.append(name)
    info['methods'] = methods



    # Дополнительная инфа (для классов)
    if inspect.isclass(obj):
        info['bases'] = [base.__name__ for base in obj.__bases__]  # Базовые классы



    return info


# Пример использования:

class MyClass:
    def __init__(self, value):
        self.my_attr = value

    def my_method(self):
        print("Hello from my_method!")


my_object = MyClass(42)

obj_info = introspection_info(my_object)
print(obj_info)

number_info = introspection_info(42)
print(number_info)


# Ещё пример (со строкой):

string_info = introspection_info("Hello, world!")
print(string_info)
