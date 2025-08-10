import requests

r = requests.get("https://bored-api.appbrewery.com/random")

data=r.json()
print(f"Activity: {data['activity']}")
print(f"Type: {data['type']}")
print(f"Participants: {data['participants']}")
print(f"Duration: {data['duration']}")
print(f"Price: {data['price']}")
print(f"Accessibility: {data['accessibility']}")