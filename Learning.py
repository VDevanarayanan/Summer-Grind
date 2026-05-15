import requests
city = input("Enter city: ")
url = f"https://wttr.in/{city}?format=j1"
response = requests.get(url)
data = response.json()
temp = data["current_condition"][0]["temp_C"]
hum = data["current_condition"][0]["humidity"]
print(f"Temperature in {city}:{temp}\n")
print(hum)
