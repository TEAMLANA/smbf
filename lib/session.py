import requests 
ses = requests.Session()
from bs4 import BeautifulSoup as parser
class browser:
    def __init__(self,kuki):
        self.__kuki = {"cookie":kuki}
    def get(self,link):
        return parser(ses.get("https://free.facebook.com" + link,cookies=self.__kuki).content,"html.parser")
