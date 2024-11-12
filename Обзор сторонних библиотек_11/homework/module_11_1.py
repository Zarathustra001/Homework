import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter
from mpl_toolkits.mplot3d import Axes3D
# Requests: работа с HTTP-запросами
print("Работа с requests:")

# 1. GET-запрос к API: получаем данные с сервера
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(f"GET-запрос: {response.status_code}")  # Выводим статус-код ответа (200 - OK, 404 - Not Found, и т.д.)
print(response.json())  # Выводим полученные данные в формате JSON

# 2. POST-запрос с данными: отправляем данные на сервер
data = {'userId': 1, 'title': 'Купить молоко', 'completed': False}
response = requests.post("https://jsonplaceholder.typicode.com/todos", json=data)
print(f"\nPOST-запрос: {response.status_code}")
print(response.json())  # Выводим ответ сервера (обычно содержит информацию о созданном объекте)

# 3. Работа с заголовками: отправляем дополнительные данные в запросе
headers = {'User-Agent': 'My Custom User Agent'}  # Задаём пользовательский User-Agent
response = requests.get("https://httpbin.org/headers", headers=headers)
print("\nЗаголовки:")
print(response.json())  # Выводим полученные заголовки


# Matplotlib: построение графиков
print("\n\nРабота с matplotlib:")

# 1. Линейный график: строим график функции sin(x)
x = np.linspace(0, 10, 100)  # Создаём массив значений x от 0 до 10 (100 точек)
y = np.sin(x)  # Вычисляем значения sin(x)
plt.plot(x, y, label='sin(x)')  # Строим график
plt.xlabel('x')  # Подписываем ось x
plt.ylabel('y')  # Подписываем ось y
plt.title('График sin(x)')  # Задаём заголовок графика
plt.legend()  # Отображаем легенду (подпись графика)
plt.show()  # Отображаем график
plt.close()

# 2. Круговая диаграмма
labels = 'Фрукты', 'Овощи', 'Злаки', 'Сладости'
sizes = [30, 45, 15, 10]  # Доли в процентах
explode = (0, 0.1, 0, 0)  # Выделяем "Овощи"

plt.figure()  # Создаём новую фигуру для круговой диаграммы
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
plt.axis('equal')  #  Чтобы круг был круглым, а не овалом
plt.title('Распределение продуктов')
plt.show()
plt.close()

# 3. 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

# Строим 3D график
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D График')
plt.show()
plt.close()


# Pillow: работа с изображениями
print("\n\nРабота с Pillow:")

try:
    img = Image.open("image.jpg")  # Пытаемся открыть файл "image.jpg"
except FileNotFoundError:
    print("Ошибка: файл image.jpg не найден. Пропускаем обработку изображений.")
else:  # Этот блок выполнится, только если файл был успешно открыт
    # 1. Изменение размера
    resized_img = img.resize((300, 200))  # Изменяем размер изображения до 300x200 пикселей

    # 2. Применение размытия
    blurred_img = img.filter(ImageFilter.BLUR)  # Применяем фильтр размытия

    # 3. Сохранение в другом формате
    resized_img.save("resized_image.png") # Сохраняем изменённое изображение в формате PNG
    blurred_img.save("blurred_image.png") # Сохраняем размытое изображение

    # Дополнительно: Поворот
    rotated_img = img.rotate(45) # Поворачиваем на 45 градусов
    rotated_img.save("rotated_image.png")

    # Дополнительно: Обрезка
    cropped_img = img.crop((100, 50, 400, 300))  # Обрезаем изображение (left, upper, right, lower)
    cropped_img.save("cropped_image.png")

    print("Изображение обработано и сохранено.")

print("\nЗавершено!")