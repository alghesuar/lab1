from bs4 import BeautifulSoup
import urllib.request
import os

BASE_URL = "https://pixabay.com/ru/editors_choice/"


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_page_count(html):
    soup = BeautifulSoup(html, "html.parser")
    paggination = soup.find('div', {"class": "paginator"})
    return int(paggination.find_all('a')[-2].text)


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    div = soup.find('div', {"class": "clearfix"})
    tagimg = div.find_all('img')
    image = []
    for img in tagimg:
        image.append(img.get('src'))

    print(image)
    return image


def create_directory(namedirectory):
    path = "Directory" + str(namedirectory)
    os.mkdir(path)
    return path


def download_image(srcimage, numberdirectory):
    # incarcarea imaginii
    pathdir = create_directory(numberdirectory)
    for numberimage in range(0, 3):
        resource = urllib.request.urlopen(srcimage[numberimage])
        path = pathdir + "\imag" + str(numberimage) + ".jpg"
        out = open(path, 'wb')
        out.write(resource.read())
        out.close()


page_count = get_page_count(get_html(BASE_URL))
print("Introduceti numarul de pagini nu mai mult de", page_count)
counter = int(input())
counter = counter + 1

for page in range(1, counter):
    URL = BASE_URL + "?media_type=photo&pagi=" + str(page)
    download_image(parse(get_html(URL)), page)
