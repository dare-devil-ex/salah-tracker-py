import requests as r
import tkinter as tk
from tkinter import messagebox

def get_prayer_timings():
    city = city_entry.get()
    country = country_entry.get()
    
    if not city or not country:
        messagebox.showerror("Input Error", "Please enter both city and country.")
        return
    
    # API URL
    data = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8"
    
    try:
        raw = r.get(data).json()["data"]["timings"]
        
        fajr_label.config(text=f"Fajr: {raw['Fajr']}")
        dhuhr_label.config(text=f"Dhuhr: {raw['Dhuhr']}")
        asr_label.config(text=f"Asr: {raw['Asr']}")
        maghrib_label.config(text=f"Maghrib: {raw['Maghrib']}")
        isha_label.config(text=f"Isha: {raw['Isha']}")
        imsak_label.config(text=f"Imsak: {raw['Imsak']}")
        sunrise_label.config(text=f"Sunrise: {raw['Sunrise']}")
        sunset_label.config(text=f"Sunset: {raw['Sunset']}")
        midnight_label.config(text=f"Midnight: {raw['Midnight']}")
        firstthird_label.config(text=f"First Third: {raw['Firstthird']}")
        lastthird_label.config(text=f"Last Third: {raw['Lastthird']}")
    except Exception as e:
        messagebox.showerror("API Error", f"An error occurred while fetching the data: {e}")

root = tk.Tk()
root.title("Prayer Timings Finder")

city_label = tk.Label(root, text="Enter City:")
city_label.grid(row=0, column=0, padx=10, pady=5)

city_entry = tk.Entry(root)
city_entry.grid(row=0, column=1, padx=10, pady=5)

country_label = tk.Label(root, text="Enter Country:")
country_label.grid(row=1, column=0, padx=10, pady=5)

country_entry = tk.Entry(root)
country_entry.grid(row=1, column=1, padx=10, pady=5)

fetch_button = tk.Button(root, text="Get Prayer Timings", command=get_prayer_timings)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)

fajr_label = tk.Label(root, text="Fajr: ")
fajr_label.grid(row=3, column=0, columnspan=2, pady=2)

dhuhr_label = tk.Label(root, text="Dhuhr: ")
dhuhr_label.grid(row=4, column=0, columnspan=2, pady=2)

asr_label = tk.Label(root, text="Asr: ")
asr_label.grid(row=5, column=0, columnspan=2, pady=2)

maghrib_label = tk.Label(root, text="Maghrib: ")
maghrib_label.grid(row=6, column=0, columnspan=2, pady=2)

isha_label = tk.Label(root, text="Isha: ")
isha_label.grid(row=7, column=0, columnspan=2, pady=2)

imsak_label = tk.Label(root, text="Imsak: ")
imsak_label.grid(row=8, column=0, columnspan=2, pady=2)

sunrise_label = tk.Label(root, text="Sunrise: ")
sunrise_label.grid(row=9, column=0, columnspan=2, pady=2)

sunset_label = tk.Label(root, text="Sunset: ")
sunset_label.grid(row=10, column=0, columnspan=2, pady=2)

midnight_label = tk.Label(root, text="Midnight: ")
midnight_label.grid(row=11, column=0, columnspan=2, pady=2)

firstthird_label = tk.Label(root, text="First Third: ")
firstthird_label.grid(row=12, column=0, columnspan=2, pady=2)

lastthird_label = tk.Label(root, text="Last Third: ")
lastthird_label.grid(row=13, column=0, columnspan=2, pady=2)

root.mainloop()
