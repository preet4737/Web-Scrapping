from bs4 import BeautifulSoup
import requests
from io import BytesIO
from PIL import Image

search = input("What do you want to search:").strip()
p = {"q" : search}
r = requests.get("https://www.google.co.in/search?", params= p)

soup = BeautifulSoup(r.text, "html.parser")


