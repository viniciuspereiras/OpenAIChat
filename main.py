import requests
import sys
import json

def do_request(data_text):
  """
  Paste your burp request here using "Burp to python requests" extensions.
   - You need to change burp_json like in example of README.md
  """
  burp0_url = "https://chat.openai.com:443/backend-api/conversation"
  burp0_cookies = ... 
  burp0_headers = ...                                                                                
  burp0_json= ...
  return requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json).text

def scrap_response(response):
    text = response[:-14]
    index = text.rfind("{\"message")
    return json.loads(text[index:])

elon_musk = scrap_response(do_request(record()))
print(elon_musk["message"]["content"]["parts"][0])
