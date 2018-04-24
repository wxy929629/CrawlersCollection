from urllib.error import HTTPError
from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
通过urllib的request模块请求url,获取beautifulsoup对象
'''
def get_beautifulSoup(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
    else:
        if html is None:
            print("URL is not found")
            return None
        else:
            bs_obj = BeautifulSoup(html.read(), "html.parser")
            return bs_obj
