import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
url ="https://www.imdb.com/india/top-rated-indian-movies/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tags = soup.find_all("td", class_="titleColumn")
tags1 = soup.find_all("span", class_="secondaryInfo")
print(tags)
#print(tags1)
movieYear = []
for tag in tags1:
    movies = tag.text
    movieYear.append(movies)
print(movieYear)
print(len(movieYear))
print("===============")

Title1 = []
for tag in tags:
    movie = tag.text.strip()
    Title1.append(movie)
print(Title1)
movieTitle = []
for i in Title1:
    movieTitle2 = i[:-7:1][9::1]
    movieTitle.append(movieTitle2)
print(movieTitle)
print(len(movieTitle))

plt.hist(movieYear,30)
plt.xlim(0,20)
#plt.xlim(0,11)
plt.ylim(0,30)
plt.show()



