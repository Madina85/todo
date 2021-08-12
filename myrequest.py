from requests import get

response = get("https://vk.com/")

print(response.text)