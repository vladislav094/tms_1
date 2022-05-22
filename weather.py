# from tkinter import *
import argparse
# import requests
#
# root = Tk()
# root.geometry('350x350')
#
# def get_weather():
#     city = cityField.get()
#     key = 'c3fc20f6feabb80fbc39037e91a87b43'
#     url = 'https://api.openweathermap.org/data/2.5/weather'
#     params = {'APPID': key, 'q': city, 'units': 'metric'}
#     result = requests.get(url, params=params)
#     weather = result.json()
#     info['text'] = f'Now in {str(weather["name"])}: {weather["main"]["temp"]}'
#     root['bg'] = '#fafafa'
#     root.title('Weather for you')
#     root.geometry('350x350')
#     root.resizable(width=False, height=False)
#
# frame_information = Frame(root, bg='orange', bd=5)
# frame_information.place(relx=0.15, rely=0.00, relwidth=0.7, relheight=0.1)
# frame_lable = Frame(root, bg='orange', bd=0)
# frame_lable.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.1)
# lable = Label(frame_lable, text="Введите название города", bg='orange', font=100)
# lable.pack()
# # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
# frame_input = Frame(root, bg='orange', bd=0)
# # Также указываем его расположение
# frame_input.place(relx=0.15, rely=0.22, relwidth=0.7, relheight=0.25)
# # Создаем текстовое поле для получения данных от пользователя.
# info = Label(frame_information, text='Погодная информация', bg='orange', font=100)
# info.pack()
# cityField = Entry(frame_input, bg='white', font=70)
# cityField.pack()
# # Размещение этого объекта, всегда нужно прописывать
# # Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
# btn = Button(frame_input, text='Узнать погоду', command=get_weather)
# btn.pack()
# # Запускаем постоянный цикл, чтобы программа работала
# root.mainloop()


def get_weather(city):
    # city = cityField.get()
    key = 'c3fc20f6feabb80fbc39037e91a87b43'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()
    # print(weather)
    return weather

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("a")
    args = parser.parse_args()
    print(args.a)
    print(get_weather(args.a))