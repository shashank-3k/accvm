import base64
import json                    
import numpy as np
import requests

api = 'http://localhost:5001/processImage'
image_file = 'labrador.jpg'
with open(image_file, "rb") as f:
    im_bytes = f.read()        
im_b64 = base64.b64encode(im_bytes).decode("utf8")

payload = json.dumps({"image": im_b64})
response = requests.post(api, json=payload)
try:
    data = response.json()     
    print(data)                
except requests.exceptions.RequestException:
    print(response.text)