import requests # a lib for making HTTP requests
import json # a lib for working with JSON data

url = "https://flask-app-demo.onrender.com/predict?level=Junior&lang=Java&tweets=yes&phd=no"

# make the HTTP GET request
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
response = requests.get(url)

# first thing, check the response's status code
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
print(response.status_code)
if response.status_code == 200:
    # OK (success)
    # we can parse the JSON response in the message body
    json_dict = json.loads(response.text)
    print(json_dict)
    pred = json_dict["prediction"]
    print("prediction:", pred)