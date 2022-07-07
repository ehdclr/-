from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
django.setup()

from stock.models import Product


def parse_product():
    baseUrl = "https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query="
    plusUrl ="향수"
    # plusUrl = input("검색할 상품의 이름을 입력하세요 :")
    url = baseUrl + quote_plus(plusUrl)
    print(url)

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'User-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
    chrome_options.add_argument("lang=ko_KR")
    driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
    driver.get(url)

    html = driver.page_source
    soup1 = BeautifulSoup(html)
    data = {}
    products = 1

    while products < 5:
        link = '//*[@id="w_cate_prd_list"]/li[{0}]/div/div/a/p'.format(products)
        item = driver.find_element_by_xpath(link).click()
        driver.implicitly_wait(20)
        product_name = driver.find_element_by_class_name('prd_name')
        product_price = driver.find_element_by_class_name('price-2')
        product_rate = driver.find_element_by_css_selector('#repReview > b')
        product_reviews = driver.find_element_by_css_selector('#repReview > em')
        data['product'] = product_name.text
        data['price'] = product_price.text
        data['rate'] = product_rate.text
        data['review'] = product_reviews.text
        driver.back()
        return data
        products = products + 1
    if __name__ =='__main__':
        product_data_dict= parse_product()
        for t,l,k,a in product_data_dict.items():
            Product(product=t,price=l,rates=k,reviews=a).save()
















