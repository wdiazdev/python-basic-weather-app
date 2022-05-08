import requests


api_key = "YOUR KEY HERE"
base_url = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

# To request a city 
request_url = f"{base_url}?appid={api_key}&q={city}"

# To get the request
response = requests.get(request_url)

# To make sure the request was OK
if response.status_code == 200:
    data = response.json()

    weather = data['weather'][0]['description']
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    temp_fahrenheit = round((temp_kelvin - 273.15) * 9 / 5 + 32, 2)

    print('Weather: ', weather)
    print('Temperature: ', temp_fahrenheit, 'Fahrenheit')

else:
    print("An error occurred.")
