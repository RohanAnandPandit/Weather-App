# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 22:27:32 2020

@author: rohan
"""
from App import App
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1)
from utils import city_data, data_from_coord

print("\n=========WEATHER APP=========\n")
print('Type the name of a city', end = '')
print (' or give the longitude and latitude as "<lon>,<lat>"\n')
print('Type "quit" to exit. Type "gui" to launch app.\n')

while True:
    inp = input('>> ')
    if inp == 'quit': break
    if inp == 'gui': App().start(); continue
    try:
        if ',' in inp:
            lon, lat = inp.split(',')
            info = data_from_coord(lon, lat)
        else:
            info = city_data(inp)
    except:
        print("Unable to get data")
        continue
    for field in info.keys():
        print(field, ':', info[field])
