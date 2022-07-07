from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market.settings")
import django
django.setup()

from stock import models

# olive.py 에서는 먼저 상품 검색하고 결과 화면 링크 까지 나오도록.

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f'User-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36')
chrome_options.add_argument("lang=ko_KR")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe', chrome_options = chrome_options)

url = 'https://www.oliveyoung.co.kr/'
driver.get(url)
xpath = "//input[@id='query']"

keyword =input("검색어를 입력하세요 : ")
print()
driver.find_element_by_xpath(xpath).send_keys(keyword+'\n')

# result_page = input("이동 페이지 (숫자만) 입력 : ")
result = "https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=" + keyword + "&giftYn=N"
# result는 전체 검색 결과 페이지를 보여줌

print("전체 검색 결과 페이지: ", result)
print()

# 검색결과 페이지
result_page = 'https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query' + keyword +'=&giftYn=N'
res1 = requests.get(result_page)
soup1 = BeautifulSoup(res1.text, "lxml")


# 이동할 페이지 링크 출력
link = driver.find_element_by_xpath('//*[@id="w_cate_prd_list"]/li[1]/div/a')
item_url = link.get_attribute('href')
print("이동할 링크 : ",item_url)
print()

# 첫번째 상품 페이지로 이동
item = driver.find_element_by_xpath('//*[@id="w_cate_prd_list"]/li[1]/div/div/a/p').click()

# 상품 페이지 내에서의 크롤링 부분 // 이름, 가격, 별점
item_page = item_url

driver.get(item_url)
res2 = requests.get(item_url)
soup2 = BeautifulSoup(res2.text, "lxml")


item_page = driver.find_elements_by_xpath('//*[@id="Container"]') 
for info in item_page:
    name = soup2.find("p", attrs={"class":"prd_name"}).get_text()
    print("상품명 : ", name.strip()) # strip => 양쪽 공백 제거
    price = soup2.find("span", attrs={"class":"price-2"}).get_text()
    print("상품 가격 : ", price.strip())

item_page2 = driver.find_elements_by_xpath('//*[@id="repReview"]')
for info2 in item_page2:
    rate = soup2.find("b").get_text() # 평점 
    num = soup2.find("em").get_text() # 리뷰 수
    print("상품 평점 : ", rate.strip(), num.strip())


item2 = driver.find_element_by_xpath('//*[@id="reviewInfo"]/a').click()
for x in range(1,6):
    item_page3 = driver.find_elements_by_xpath('//*[@id="gdasContentsArea"]/div/div[1]/div/div[3]/ul/li[{0}]'.format(x))
    for info2 in item_page3:
        percent = soup2.find("span",attrs={"class":"per"}).get_text()
        print("{0} : ".format(x), percent)


'''
name = driver.find_element_by_xpath('//*[@id="Contents"]/div[2]/div[2]/div/p[2]')
price = driver.find_element_by_xpath('//*[@id="Contents"]/div[2]/div[2]/div/div[1]/span[2]/strong')
rate = driver.find_element_by_xpath('//*[@id="repReview"]/b')
review = driver.find_element_by_xpath('//*[@id="gdasList"]/li[1]/div[2]/p')
'''


# 내용 출력
"""
print("상품명 :", name)
print("상품 가격: ", price)
print("상품 별점: ", rate)
print("상품 한줄평:", review)
"""

#for title in goods:
#    name = soup.find("p", attrs={"class":"flag li_result"}).get_text()
#    print(name.get_text())



# items = soup.find_all("li", attrs={"class":"flag li_result"})


"""

for result_link in items:
    name = soup.find_all("p", attrs={"class":"tx_name"})
    print("검색된 아이템 : ", name)

    price = soup.find_all("span", attrs={"class":"tx_num"})
    print("아이템 가격 : ", price)

    a = items.find()("a", attrs={"class":"flag li_result"})
    link = a.get('href')
    print("아이템 링크: ", link)

#######

for item in items:
    name = item.find("p", attrs={"class":"tx_name"}).get_text() # 상품 이름
    price = item.find("span", attrs={"class":"tx_num"}).get_text()  # 상품 가격
    rate =  # 상품 별점
    review =  # 상품 리뷰 

link = item.find("a", attrs={"class":""})["href"]
# https://www.oliveyoung.co.kr/store/goods/


"""






"""

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()

chrome_options.add_argument(f'User-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36')
chrome_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome('C:\web test\chromedriver.exe',chrome_options=chrome_options)

url = 'https://www.oliveyoung.co.kr/'

driver.get(url)

xpath = "//input[@id='query']"

keyword =input("검색어를 입력하세요 : ")

driver.find_element_by_xpath(xpath).send_keys(keyword+'\n')



"""