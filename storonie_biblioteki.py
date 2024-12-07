
import requests
import matplotlib
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

# Библиотека Python Requests — это библиотека, которая
# создана для быстрой и простой работы с запросами.
requests.get('https://skillbox.ru')
res = requests.get('https://skillbox.ru') # Создаём переменную, в которую
# сохраним код состояния запрашиваемой страницы.
print(res) # Выводим код состояния.

'''
Коды состояний имеют вид трёхзначных чисел от 100 до 500. Чаще всего встречаются 
следующие:

200 — «OK». Запрос прошёл успешно, и мы получили ответ.
400 — «Плохой запрос». Его получаем тогда, когда сервер не может понять запрос, отправленный клиентом. Как правило, это указывает на неправильный синтаксис запроса, неправильное оформление сообщения запроса и так далее.
401 — «Unauthorized». Для выполнения запроса необходимы актуальные учётные данные.
403 — «Forbidden». Сервер понял запрос, но не может его выполнить. Например, у используемой учётной записи нет достаточных прав для просмотра содержимого.
'''
'''
Matplotlib отображает ваши данные на Figures (например, окна, виджеты Jupyter 
и т. д.), каждый из которых может содержать один или несколько Axes, область, 
где точки могут быть указаны в терминах координат xy (или theta-r в полярном 
графике, xyz в 3D-графике и т. д.)
'''
# Пример из библиотеки matplotlib
fig, ax = plt.subplots()             # Создайте фигуру содержащую одну ось.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Внесите данные на оси.
plt.show()                           # Покажите рисунок.
# Изменяем данные
fig, ax = plt.subplots()             # Создайте фигуру содержащую одну ось.
ax.plot([1, 3, 2, 1], [1, 2, 4, 3])  # Внесите данные на оси.
plt.show()                           # Покажите рисунок.


# Пример из библиотеки matplotlib
plt.style.use('_mpl-gallery')

# Make data
n = 100
xs = np.linspace(0, 1, n)
ys = np.sin(xs * 6 * np.pi)
zs = np.cos(xs * 6 * np.pi)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(xs, ys, zs)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
# Изменяем данные
plt.style.use('_mpl-gallery')

# Make data
n = 300
xs = np.linspace(0, 1, n)
ys = np.sin(xs * 12 * np.pi)
zs = np.cos(xs * 12 * np.pi)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(xs, ys, zs)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()

# Пример из библиотеки matplotlib

plt.style.use('_mpl-gallery')

# Make data
X, Y, Z = axes3d.get_test_data(0.05)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()
# Изменяем данные
plt.style.use('_mpl-gallery')

# Make data
X, Y, Z = axes3d.get_test_data(0.06)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_wireframe(X, Y, Z, rstride=25, cstride=25)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()

'''
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas,
 numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их
основными возможностями и функциями. К каждой библиотеке дана ссылка на
документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных
(на своё усмотрение) и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом
и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас
 инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить
 эффекты и сохранить в другой формат.
В приложении к ссылке на GitHub напишите комментарий о возможностях, которые
предоставила вам выбранная библиотека и как вы расширили возможности Python с
её помощью.
Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из
каждой выбранной

'''