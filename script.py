import requests

r = requests.get("https://raw.githubusercontent.com/Jmmxp/CMPUT404-Lab1/main/script.py")
print(r.text)
