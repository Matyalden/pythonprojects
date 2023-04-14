import requests

response = requests.get("https://randomfox.ca/floof/")

print(response.status_code) #200 ok
print(response.text) #text api

'''{"image":"https:\/\/randomfox.ca\/images\/87.jpg",
"link":"https:\/\/randomfox.ca\/?i=87"}
'''

print(response.json()['image']) #text json

 

