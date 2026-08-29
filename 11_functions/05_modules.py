# There are two types of modules in python:
# - Built in modules
# - External modules
# List of all built in modules: https://docs.python.org/3/py-modindex.html
import math
import os # Bluriness of module says you imported it but didn't used it
import mymodule
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)