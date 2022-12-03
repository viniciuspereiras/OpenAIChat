# OpenAIChat
An unofficial, and completely bad client (keep in mind it's a weird way of doing this) to use OpenAI's chat in python, feel free to add it to your projects, implement speech recognition, text to speach and whatever something else you think is cool.

# How to configure 
- Open your burp suite browser, log into your account and go to chat page
- Turn on the interceptation of the requests, send a message in chat
- Do some fowards and when this endpoint appears:

![alt text](https://raw.githubusercontent.com/viniciuspereiras/OpenAIChat/main/end-point.png)

- Send to repeater, now click with right button -> extensions -> Copy as python requests
- Open main.py file and Ctrl+V into do_request()
- Now you need to change somethings:
```python
json={"action": "variant", "conversation_id": "...", "messages": [{"content": {"content_type": "text", "parts": ["MESSAGE"]}, "id": "...", "role": "user"}], "model": "...", "parent_message_id": "..."}
#change to:
json={"action": "variant", "conversation_id": "...", "messages": [{"content": {"content_type": "text", "parts": [data_text]}, "id": "...", "role": "user"}], "model": "...", "parent_message_id": "..."}
```
and 
```python
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
#change to:
return requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json).text
```
# How to use 
As you want :)
- `python3 main.py "Hello World"`

This will work because in script the input is `sys.argv[1]` ;) 
