import json
import requests
data=requests.get("https://reqres.in/api/users?page=2")
ExtractedData=data.json()
print(ExtractedData)