import requests
from bs4 import BeautifulSoup
ur_link = ("https://realpython.github.io/fake-jobs/")
page = requests.get(ur_link)


vle = BeautifulSoup(page.content, "html.parser")

result = vle.find(id="ResultsContainer")

print(result.content)
