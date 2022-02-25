from time import sleep
import requests
from bs4 import BeautifulSoup


class Crawler():
    def __init__(self) -> None:
        pass

    def test(self, stockID):
        response = requests.get(
            "https://s.yimg.com/nb/tw_stock_frontend/scripts/TaChart/tachart.3de240ea9a.html?sid="+str(stockID))
        soup = BeautifulSoup(response.text, "html.parser")

        print(soup)  # 輸出排版後的HTML內容
