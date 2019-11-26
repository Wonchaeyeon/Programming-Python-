#터미널 > pip install bs4
#터미널 > pip install lxml

from bs4 import BeautifulSoup       #html구조적으로 변환하자
from urllib.request import urlopen  #url에 해당하는 html 가져오자.

if __name__ == '__main__':
   # 네이버 웹툰 > 신의탐 제목 가져오자
   #  data=urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=183559&weekday=mon")  
    data=urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=703846&weekday=tue")  #여신강림
    soup=BeautifulSoup(data,"lxml")
    # print(soup)
    cartoon_titles=soup.find_all("td",attrs={"class":"title"})    #<td class="title">
    html="<html><head><meta charset='utf-8'></head><body>"
    for title in cartoon_titles[:]:        #find는 하나만 가져옴. find_all은 리스트를 다 가져오는 것임
        t=title.find("a").text          #제목 가져오자
        link=title.find("a").get("href")    #링크 가져오자
        link = "https://comic.naver.com/"+link
        # print(t)
        # print(link)
        # print("<a href="+link+">"+t+"</a>")
        html+="<a href="+link+">"+t+"</a><br />"
    html+="</body></html>"
    outputSoup=BeautifulSoup(html,"lxml")       #html
    prettyHtml=str(outputSoup.prettify())
    with open("여신강림.html","w",encoding="utf-8") as f:
        f.write(prettyHtml)