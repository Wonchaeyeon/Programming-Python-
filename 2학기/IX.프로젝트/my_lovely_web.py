#영풍문고 베스트셀러
from urllib.request import urlopen
from bs4 import BeautifulSoup

if __name__ == '__main__':
    with urlopen("https://www.ypbooks.co.kr/m_bestseller.yp") as data:
        soup = BeautifulSoup(data, "lxml")
    #print(soup)
    books_titles = soup.find_all("span", attrs={"class": "info-tit"})

    print("[영풍문고 베스트셀러]")
    n=1
    for books_title in books_titles:
        print(n,books_title.text)
        n+=1







