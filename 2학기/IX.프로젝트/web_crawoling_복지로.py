from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url="http://bokjiro.go.kr/welInfo/retrieveWelInfoBoxList.do"
    data = {"searchIntClId":"01","pageUnit":"300"}
    with requests.post(url,data) as response:
        soup = BeautifulSoup(response.text,"lxml")

    # print(soup)
    # <dt class="tit"><a href="javascript:fn_move('999','164')">아이돌봄서비스</a></dt>
    # dts = soup.find_all("dt",attrs={"class":"tit"})
    # for dt in dts:
    #     title=dt.find("a")
    #     print(title.text)

    # 위에 긴걸 아래 짧게 쓸 수 있음
    n=1
    titles = soup.select("dt.tit > a") #<dt class = "tit"><a>text</a></dt>
    for title in titles:
        print(n,title.text)
        n+=1