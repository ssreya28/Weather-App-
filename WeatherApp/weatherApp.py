import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/en-IN/weather/today/l/e589cb963d38f2fec57e0bf3596c8a33e17ded62f23b8cd83376fcdd89a820d1"

master = Tk()
master.title("Weather App")
master.config(bg = "white")

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    location = soup.find('h1', class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find('span', class_="CurrentConditions--tempValue--MHmYY").text
    weatherPredict = soup.find('div', class_="CurrentConditions--phraseValue--mZC_p").text

    locationLabel.config(text=location)
    tempLabel.config(text=temperature)
    weatherPredictLabel.config(text=weatherPredict)

    tempLabel.after(60000, getWeather)
    master.update()

img = Image.open("C:/Users/Sreya Srungarapu/Desktop/image.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

locationLabel = Label(master, font=("Calibri bold", 20), bg="white")
locationLabel.grid(row=0, sticky="N", padx=100)
tempLabel = Label(master, font=("Calibri bold", 70), bg="white")
tempLabel.grid(row=1, sticky="W", padx=40)
Label(master, image=img, bg="white").grid(row=1, sticky="E")
weatherPredictLabel = Label(master, font=("Calibri bold", 15), bg="white")
weatherPredictLabel.grid(row=2, sticky="W", padx=40)
getWeather()

master.mainloop()
