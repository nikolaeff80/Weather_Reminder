import requests

from tkinter import *

root = Tk()
bg = '#fafafa'


def get_weather():
	city = 'Moscow'
	key = '626e5a8c41ef4cfa75a98c6905b10b60'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': key, 'q': city, 'units': 'metric'}
	result = requests.get(url, params=params)
	weather = result.json()
	# weather["main"]["temp"] = -4.85  # Для тестовой отладки
	
	if weather["main"]["temp"] > -4.5:
		info_condition_yes = Label(frame_last, text='Кондиционер', bg='#fafafa', fg="green", font=40)
		info_condition_yes.pack()
		info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
		info_condition_yes['text'] = 'Можно использовать кондиционер'
	else:
		info_condition_no = Label(frame_last, text='Кондиционер', bg='#fafafa', fg='red', font=40)
		info_condition_no.pack()
		info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
		info_condition_no['text'] = 'Нельзя использовать кондиционер'


root['bg'] = '#fafafa'
root.title('Погода')
root.geometry('380x150')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#fafafa', bd=1)
frame_top.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.25)
frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.35, relwidth=0.7, relheight=0.2)
frame_last = Frame(root, bg=bg, bd=5)
frame_last.place(relx=0.15, rely=0.7, relwidth=0.7, relheight=0.2)

btn = Button(frame_top, text='Проверить погоду', command=get_weather)
btn.pack()

info = Label(frame_bottom, text='Погодная информация', bg='#ffb700', font=40)
info.pack()

root.mainloop()
