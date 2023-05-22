from tkinter import *
import requests # библиотека для работы с отправкой URL запросов
root = Tk() # Создаем главный объект (окно приложения)
# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    city = cityField.get() # Получаем данные от пользователя
    # данные о погоде будем брать с сайта openweathermap.org
    key = '9de276cc4c216cf8f5d3c59add5d0421'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # Доп. параметры (ключ, город и единицы измерения)
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params) # Отправляем запрос по URL
    weather = result.json() # Получаем JSON ответ по этому URL
    # Полученные данные выводим в текстовую надпись
    info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
# Настройки главного окна
root['bg'] = '#fafafa' # фоновый цвет
root.title('Погодное приложение') # название окна
root.geometry('300x250') # размеры окна
root.resizable(width=False, height=False)
# Создаем фрейм (область для размещения других объектов)
frame_top = Frame(root, bg='#ffb700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)
# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)
# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=30)
cityField.pack() # Размещение текстового поля
# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть погоду', command=get_weather)
btn.pack()
# Создаем текстовую надпись, в кот. выведем информацию о погоде
info = Label(frame_bottom, text='Погода в городе', bg='#ffb700', font=40)
info.pack()
# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()