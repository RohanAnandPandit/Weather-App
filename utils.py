# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 18:52:13 2020

@author: rohan
"""
import requests
from PIL import Image, ImageTk

  
# API key
api_key = "2e2a0c6cd657efd2df7e20cbae5ceeac"
  
# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"+"appid="+api_key 
  
def city_data(city_name):
    """Gathers weather data by making API call from the name of the city."""
    complete_url = base_url + "&q=" + city_name + '&units=metric' 
    response = requests.get(complete_url)
    return extract_data(response.json())

def data_from_coord(lon, lat):
    """Gathers weather data from the longitude and latitude strings."""
    complete_url = base_url + '&lat=' + lat + '&lon=' + lon + '&units=metric' 
    response = requests.get(complete_url)
    return extract_data(response.json())

def extract_data(data):
    """Returns dictionary with useful weather data points."""
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_max = data['main']['temp_max'] 
    temp_min = data['main']['temp_min']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    name = data['name']
    return {'Name' : name, 'Temperature' : temp,
            'Max temperature' : temp_max, 'Min temperature' : temp_min,
            'Humidity' : humidity, 'Description' : description, 
            'Pressure' : pressure, 'Feels like' : feels_like, 
            'Wind speed' : wind_speed} 

def rgb_to_hex(rgb):
    """Translates an rgb tuple of int to a tkinter friendly color code"""
    return "#%02x%02x%02x" % rgb

def get_image(filename):
    return ImageTk.PhotoImage(Image.open(filename), Image.ANTIALIAS)