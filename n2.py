from tkinter import *
import requests # библиотека для работы с отправкой URL запросов
root = Tk() # Создаем главный объект (окно приложения)
# Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
def get_weather():
    city = cityField.get() # Получаем данные от пользователя
    key = '9de276cc4c216cf8f5d3c59add5d0421'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    # Доп. параметры
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params) # Отправляем запрос по URL
    weather = result.json() # Получаем JSON ответ по этому URL
    # Полученные данные выводим в текстовую надпись
    info['text'] = f'{str(weather["name"])}: {weather["weather"][0]["main"]}, {weather["weather"][0]["description"]}'
# Настройки главного окна
root['bg'] = '#FFA07A' # фоновый цвет
root.title('Погодное приложение') # название окна
root.geometry('350x250') # размеры окна
root.resizable(width=False, height=False)
# Создаем фрейм (область для размещения других объектов)
frame_top = Frame(root, bg='#FFA07A', bd=5)
frame_top.place(relx=0.10, rely=0.15, relwidth=0.8, relheight=0.25)
# Все то-же самое, но для второго фрейма
frame_bottom = Frame(root, bg='#7FFFD4', bd=5)
frame_bottom.place(relx=0.10, rely=0.55, relwidth=0.8, relheight=0.1)
# Создаем текстовое поле для получения данных от пользователя
cityField = Entry(frame_top, bg='white', font=20)
cityField.pack() # Размещение текстового поля
# Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
btn = Button(frame_top, text='Посмотреть осадки', command=get_weather)
btn.pack()
# Создаем текстовую надпись, в кот. выведем информацию о погоде
info = Label(frame_bottom, text='Осадки в городе', bg='#7FFFD4', font=20)
info.pack()
# Запускаем постоянный цикл, чтобы программа работала
root.mainloop()