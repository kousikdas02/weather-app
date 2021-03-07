import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)
    
#6f899d32103ebef40f5d31846fe17dcf
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def format_response(weather):
    try:
        name = weather['name']
        description = weather['weather'][0]['description']
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s \nHumidity: %s \nWind Speed: %s /m' % (name, description, temp, humidity, wind)

    except:
        final_str = 'There is a problem retrieving that information'

    return final_str

def get_weather(city):
    weather_key = '6f899d32103ebef40f5d31846fe17dcf'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    
    lable['text'] = format_response(weather)


root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg = '#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')


entry = tk.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text = "Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=7)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


lable = tk.Label(lower_frame, font=('Courier', 18))
lable.place(relwidth=1, relheight=1)


root.mainloop()