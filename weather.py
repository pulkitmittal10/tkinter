from tkinter import *
from PIL import ImageTk, Image
import requests
import json

root = Tk()
root.title('Weather')
# root.geometry('300x30')

try:
	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=0E466704-C530-4042-A2B3-EFA2C002C829")
	api = json.loads(api_request.content)
	city = api[0]['ReportingArea']
	quality = api[0]['AQI']
	category = api[0]['Category']['Name']

	if category == "Good":
		weather_color = "#0C0"
	elif category == "Moderate":
		weather_color = "#FFFF00"
	elif category == "Unhealthy for Sensitive Groups":
		weather_color = "#ff9900"
	elif category == "Unhealthy":
		weather_color = "#FF0000"
	elif category == "Very Unhealthy":
		weather_color = "#990066"
	elif category == "Hazardous":
		weather_color = "#660000"

	myLabel = Label(root, text=city + " Air Quality " + str(quality) + " " + category, font=("Helvectica"), background=weather_color)
	myLabel.pack()
	root.configure(background=weather_color)

except Exception as e:
	api = "Error..."

root.mainloop()