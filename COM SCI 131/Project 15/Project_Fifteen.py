# Windchill Calculator GUI

import tkinter as tk
from tkinter import *

class Application(tk.Frame):
    
    def __init__(self, master = None):
        tk.Frame.__init__(self, master)
        self.grid() # Grid layout populator
        
        title = Label(master, text= "WINDCHILL CALCULATOR",
                      font = ("Times New Roman", 16), 
                      bg = "yellow", fg = "red")
        title.grid(column = 0, row = 0, columnspan = 2)
        
        t_lbl = Label(master, text = "Enter the temperature " + 
                      "in degrees Fahrenheit: ")
        t_lbl.grid(column = 0, row = 1)
        
        t_text = Entry(master, width = 5) # Fahrenheit Temperature
        t_text.grid(column = 1, row = 1, sticky = E)
        
        w_lbl = Label(master, text = "Enter the wind speed in mph: ")
        w_lbl.grid(column = 0, row = 2)
        
        w_text = Entry(master, width = 5) # Wind Speed
        w_text.grid(column = 0, row = 2, sticky = E)
        
        result = Label(master, text = "The windchill temperature is: ")
        result.grid(column = 0, row = 4)
        
        def calculate_windchill(temperature, wind_speed):
            w = (35.74 + 0.6215 * (temperature) - 35.75 * (wind_speed**0.16) + 
                 0.4275 * temperature * (wind_speed**0.16))
            
            windchill = round(w, 1)
            return windchill
        
        def click():
            # Gather temperature/windspeed inputs
            tempg = float(t_text.get())
            windg = float(w_text.get())
            
            # Display Result
            x = str(calculate_windchill(tempg, windg))
            result.config(text = "The windchill temperature is: " + x)
        
        calculate_button = Button(master, text = "Calculate Windchill",
                                  command = click)
        calculate_button.grid(column = 0, row = 3)

master = tk.Tk()
master.title("Windchill Calculator")
master.geometry("300x125")

win = Application(master)
win.mainloop()
