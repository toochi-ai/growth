import requests


print("repeat git")

print("new local changes")

print("added another computer")


api_url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(api_url)

if response.status_code == 200:
    print(response.text)
else:
    print(response.status_code)


# api_url = "http://api.open-notify.org/iss-now.json"
# response = requests.get(api_url)
# coordinates = response.json().get("iss_position")
# formatted_coordinates = f"{coordinates['longitude']}%2C{coordinates['latitude']}"
# map_url = f"https://yandex.com/maps/?ll={formatted_coordinates}&z=10"
# print(map_url)