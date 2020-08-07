# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:34:16 2020

@author: rohan
"""
import tkinter as tk
from Map import Map, Pin
from utils import get_image, city_data

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg = 'white')
        self.width, self.height = 1500, 1200
        self.root.geometry(str(self.width) + 'x' + str(self.height) + '+0+0')
        self.root.title('Weather App')
        tk.Label(self.root, text = 'Enter name of city:').place(x = 0, y = 0)
        self.city_input = tk.Entry(self.root, width = 20, font = 'Calibri 20')
        self.city_input.place(x = 0, y = 60)
        
        button = tk.Button(self.root, text = 'Get city data',
                           command = lambda: self.show_info())
        button.place(x = 0, y = 150)
        
        self.map = self.create_map()
        self.pin = Pin(self.root, self.map, self)
        self.add_bindings()
        self.create_panels()
    
    def create_map(self):
        """Creates Map object for the App to show the world map."""
        map_width, map_height = 960, 942
        map_image = get_image('images/world-map2.png')
        map_label = tk.Label(self.root, image = map_image, relief = tk.GROOVE)
        map_label.image = map_image
        map_x, map_y = 0, 250
        return Map(self.root, map_label, map_width, map_height, map_x, map_y)

    def start(self):
        """Starts the tkinter window's mainloop."""
        self.root.mainloop()
        
    def add_bindings(self):
        """Adds keyboard and mouse bindings for the app."""
        self.map.label.bind('<Button-1>', self.pin.drop_pin) 
        self.city_input.bind('<Return>',
                             lambda event: self.show_info(city_data(self.city_input.get())))
        
    def create_panels(self):
        name = tk.Label(self.root, text = 'Name ', bg = 'white', fg = 'blue',
                        font = 'Calibri 26')
        name.place(x = 900, y = 0)
        name_panel = tk.Label(self.root, text = '______', bg = 'white', 
                              fg = 'blue', font = 'Calibri 26')
        name_panel.place(x = 1150, y = 0)
        
        
        thermometer_img = get_image('images/thermometer.png')
        thermometer = tk.Label(self.root, image = thermometer_img,
                               text = '    ', bg = 'white', fg = 'blue', 
                               font = 'Calibri 20') 
        thermometer.image = thermometer_img
        thermometer.place(x = 1000, y = 100)
        
        
        temp_panel = tk.Label(self.root, text = '°C', bg = 'white', 
                              fg = 'blue', font = 'Calibri 26')
        temp_panel.place(x = 1150, y = 100)


        max_thermometer = tk.Label(self.root, image = thermometer_img, 
                               bg = 'white', fg = 'blue', compound = 'center',
                               font = 'Calibri 20', text = "MAX")
        max_thermometer.place(x = 1000, y = 200)
        max_temp_panel = tk.Label(self.root, text = '°C', bg = 'white', 
                              fg = 'blue', font = 'Calibri 26')
        max_temp_panel.place(x = 1150, y = 200)

        min_thermometer = tk.Label(self.root, image = thermometer_img, 
                               bg = 'white', fg = 'blue', compound = 'center',
                               font = 'Calibri 20', text = "MIN")
        min_thermometer.place(x = 1000, y = 300)
        min_temp_panel = tk.Label(self.root, text = '°C', bg = 'white', 
                              fg = 'blue', font = 'Calibri 26')
        min_temp_panel.place(x = 1150, y = 300)
        
        
        self.panels = {'temp' : temp_panel, 'name' : name_panel,
                       'max_temp' : max_temp_panel, 'min_temp' : min_temp_panel}
    
    def show_info(self, data):
        self.panels['name'].configure(text = data['Name'])
        
        temp = str(data['Temperature']) + '°C'
        self.panels['temp'].configure(text = temp)
        
        max_temp = str(data['Max temperature']) + '°C'
        self.panels['max_temp'].configure(text = max_temp)
        
        min_temp = str(data['Min temperature']) + '°C'
        self.panels['min_temp'].configure(text = min_temp)
        
    
