import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import json

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.0.0.8/api/'
username = 'ignw'
password = 'ignw'

json_header = {'Content-type': 'application/json'}

payload = '''
{
   "host": {
      "kind": "IPv4Address",
      "value": "1.2.3.54"
   },
   "kind": "object#NetworkObj",
   "name": "Python_Demo_IP1",
   "objectId": "Python_Demo_IP1"
}
'''
print(payload)

# resp = requests.get(f'{url}interfaces/physical', auth=(username, password), verify=False)

# resp_dict = json.loads(resp.text)

# print(resp.status_code)

resp = requests.post(f'{url}objects/networkobjects/Python_Demo_IP1', auth=(username,password), data=payload, headers=json_header, verify=False)

print(resp.status_code)
print(resp.text)
