from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import re
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

baseUrl = "https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query="
plusUrl = input("검색할 상품의 이름을 입력하세요 :")
url = baseUrl + quote_plus(plusUrl)
print(url)

chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=1920x1080')
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument(
    f'User-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
chrome_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe', chrome_options=chrome_options)
driver.get(url)

html = driver.page_source
soup1 = BeautifulSoup(html)

print("상위 인기 24개 파싱")

name_list = []
price_list = []
rate_list = []
review_list = []

path1 = "//p[@class='tx_name']"

el_list = driver.find_elements_by_xpath(path1)

list = []
for el in el_list:
    list.append(el.text)

print(len(list))
product_number = len(list)
product_number_remainder = product_number % 4

product_number_module = product_number // 4

if product_number_remainder == 0:
    for i in range(1, product_number_module + 1):
        for products in range(1, 5):
            link = '/html/body/div[3]/div[7]/div/div[3]/ul[{0}]/li[{1}]/div/div/a/p'.format(i, products)
            item = driver.find_element_by_xpath(link).click()
            driver.implicitly_wait(10)
            product_name = driver.find_element_by_class_name('prd_name').text
            product_price = driver.find_element_by_class_name('price-2').text.replace('\n', '').replace('원',
                                                                                                        '').replace(',',
                                                                                                                    '')
            product_rate = driver.find_element_by_css_selector('#repReview > b').text
            product_review = driver.find_element_by_css_selector('#repReview > em').text.replace('(', '').replace(')',
                                                                                                                  '').replace(
                ',', '').replace('건', '')

            int_product_review = int(product_review)
            int_product_price = int(product_price)

            driver.back()

            name_list.append(product_name)
            price_list.append(int_product_price)
            rate_list.append(float(product_rate))
            review_list.append(int_product_review)

            name_series = pd.Series(name_list)
            price_series = pd.Series(price_list)
            rate_series = pd.Series(rate_list)
            review_series = pd.Series(review_list)

            summary = pd.DataFrame({
                'Name': name_series,
                'Price': price_series,
                'Star': rate_series,
                'reviews': review_series,

            })

    print(summary)






elif (product_number_remainder != 0 and product_number_module >= 1):
    for i in range(1, product_number_module + 1):
        for products in range(1, 5):
            link = '/html/body/div[3]/div[7]/div/div[3]/ul[{0}]/li[{1}]/div/div/a/p'.format(i, products)
            item = driver.find_element_by_xpath(link).click()
            driver.implicitly_wait(20)
            product_name = driver.find_element_by_class_name('prd_name').text
            product_price = driver.find_element_by_class_name('price-2').text.replace('\n', '').replace('원',
                                                                                                        '').replace(',',
                                                                                                                    '')
            product_rate = driver.find_element_by_css_selector('#repReview > b').text
            product_review = driver.find_element_by_css_selector('#repReview > em').text.replace('(', '').replace(')',
                                                                                                                  '').replace(
                ',', '').replace('건', '')

            int_product_review = int(product_review)
            int_product_price = int(product_price)

            driver.back()

            name_list.append(product_name)
            price_list.append(int_product_price)
            rate_list.append(float(product_rate))
            review_list.append(int_product_review)

            name_series = pd.Series(name_list)
            price_series = pd.Series(price_list)
            rate_series = pd.Series(rate_list)
            review_series = pd.Series(review_list)

            summary = pd.DataFrame({
                'Name': name_series,
                'Price': price_series,
                'Star': rate_series,
                'reviews': review_series,

            })
    for i in range(product_number_module + 1, product_number_module + 2):
        for products in range(1, product_number_remainder + 1):
            link = '/html/body/div[3]/div[7]/div/div[3]/ul[{0}]/li[{1}]/div/div/a/p'.format(i, products)
            item = driver.find_element_by_xpath(link).click()
            driver.implicitly_wait(20)
            product_name = driver.find_element_by_class_name('prd_name').text
            product_price = driver.find_element_by_class_name('price-2').text.replace('\n', '').replace('원',
                                                                                                        '').replace(',',
                                                                                                                    '')
            product_rate = driver.find_element_by_css_selector('#repReview > b').text
            product_review = driver.find_element_by_css_selector('#repReview > em').text.replace('(', '').replace(')',
                                                                                                                  '').replace(
                ',', '').replace('건', '')

            int_product_review = int(product_review)
            int_product_price = int(product_price)

            driver.back()

            name_list.append(product_name)
            price_list.append(int_product_price)
            rate_list.append(float(product_rate))
            review_list.append(int_product_review)

            name_series = pd.Series(name_list)
            price_series = pd.Series(price_list)
            rate_series = pd.Series(rate_list)
            review_series = pd.Series(review_list)

            summary = pd.DataFrame({
                'Name': name_series,
                'Price': price_series,
                'Star': rate_series,
                'reviews': review_series,

            })

    print(summary)
    driver.quit()




elif (product_number_remainder != 0 and product_number_module == 0):
    for i in range(1, product_number_module + 2):
        for products in range(1, product_number_remainder + 1):
            link = '/html/body/div[3]/div[7]/div/div[3]/ul[{0}]/li[{1}]/div/div/a/p'.format(i, products)
            item = driver.find_element_by_xpath(link).click()
            driver.implicitly_wait(20)
            product_name = driver.find_element_by_class_name('prd_name').text
            product_price = driver.find_element_by_class_name('price-2').text.replace('\n', '').replace('원',
                                                                                                        '').replace(',',
                                                                                                                    '')
            product_rate = driver.find_element_by_css_selector('#repReview > b').text
            product_review = driver.find_element_by_css_selector('#repReview > em').text.replace('(', '').replace(')',
                                                                                                                  '').replace(
                ',', '').replace('건', '')

            int_product_review = int(product_review)
            int_product_price = int(product_price)

            driver.back()

            name_list.append(product_name)
            price_list.append(int_product_price)
            rate_list.append(float(product_rate))
            review_list.append(int_product_review)

            name_series = pd.Series(name_list)
            price_series = pd.Series(price_list)
            rate_series = pd.Series(rate_list)
            review_series = pd.Series(review_list)

            summary = pd.DataFrame({
                'Name': name_series,
                'Price': price_series,
                'Star': rate_series,
                'reviews': review_series,
            })

    print(summary)
    driver.quit()

df_sample1 = summary.loc[:, ['Price']]

ax = df_sample1.plot(kind='bar', title='Price', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('Product Name', fontsize=12)
ax.set_ylabel('Price', fontsize=12)
ax.legend(['Price'], fontsize=12)

df_sample2 = summary.loc[:, ['Star']]

ax = df_sample2.plot(kind='bar', title='Stars Rating', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('Product Name', fontsize=12)
ax.set_ylabel('Star Rating', fontsize=12)
ax.legend(['Stars'], fontsize=12)

df_sample3 = summary.loc[:, ['reviews']]

ax = df_sample3.plot(kind='bar', title='Reviews', figsize=(12, 4), legend=True, fontsize=12)
ax.set_xlabel('Product Name', fontsize=12)
ax.set_ylabel('Reviews', fontsize=12)
ax.legend(['Reviews'], fontsize=12)


