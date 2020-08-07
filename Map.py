# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 09:52:31 2020

@author: rohan
"""

from PIL import Image, ImageTk
import tkinter as tk
from utils import data_from_coord

class Map:
    def __init__(self, window, label, width, height, x, y):
        self.window = window
        self.label = label
        self.x = x
        self.y = y
        self.label.place(x = x, y = y)
        self.width = width
        self.height = height

class Pin:
    def __init__(self, window, map_, app):
        self.app = app
        self.char = '⮟'
        self.map = map_
        self.width, self.height = 54, 80
        self.label = tk.Label(window, text = self.char, relief = tk.FLAT,
                              borderwidth = 0, bg = 'sky blue', fg = 'red',
                              font = 'Calibri 20')
        self.label.place(x = self.map.x, y = self.map.y)
        self.lon, self.lat = 0, 0
        
    def drop_pin(self, event):
        """Changes position of pin label to where the user has clicked."""
        from utils import rgb_to_hex
        gap = 20
        self.label.place(x = self.map.x + event.x +  - self.width / 2,
                         y = self.map.y + event.y + - self.height + gap)
        
        # Colour of border of label is the colour at the pixel where the
        # user clicked
        
        image = Image.open('images/world-map2.png').convert('RGB')
        colour = image.getpixel((event.x, event.y))
        self.label.configure(bg = rgb_to_hex(colour))
        
        left = event.x - self.width / 2
        upper = event.y - self.height + gap
        right = event.x + self.width / 2
        lower = event.y + gap 
        
        # The image of the label is changed to the cropped image of the region
        # where the map is covered by the label, to look transparent
        image = Image.open('images/world-map2.png')
        image = ImageTk.PhotoImage(image.crop([left, upper, right, lower]))
        self.label.configure(image = image, text = self.char,
                             compound = 'center')
        self.label.image = image
        self.label.lift()
        
        # The current latitude and longitude pointed by the pin are re-calculated
        self.calculate_cor(event)
        self.app.show_info(data_from_coord(str(self.lon), str(self.lat)))
        
    def calculate_cor(self, event):
        """Calculates latitude and longitude at the position of the pin."""
        self.lat = (90 * ((self.map.height / 2) - event.y)/(self.map.height/ 2))
        self.lon = (-180 * ((self.map.width / 2) - event.x)/(self.map.width/ 2))+10
