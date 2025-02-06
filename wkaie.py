import requests as r

city = input("Enter the city name: ")
country = input("Enter the country name: ")
data = f"http://api.aladhan.com/v1/timingsByCity?city={city}&country={country}&method=8"
raw = r.get(data).json()["data"]["timings"]

print("========================")
print("Fajr:", raw["Fajr"])
print("Dhuhr:", raw["Dhuhr"])
print("Asr:", raw["Asr"])
print("Maghrib:", raw["Maghrib"])
print("Isha:", raw["Isha"])
print("Imsak:", raw["Imsak"])
print("========================")
print("Sunrise:", raw["Sunrise"])
print("Sunset:", raw["Sunset"])
print("Midnight:", raw["Midnight"])
print("========================")
print("Firstthird:", raw["Firstthird"])
print("Lastthird:", raw["Lastthird"])
print("========================")
