# 일단 쿠팡만 /// 옥션

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
'''

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
Auction = "http://www.auction.co.kr/"
word = input("가격 비교를 할 상품을 입력하세요 : ")

driver = webdriver.Chrome('chromedriver')
driver.get(Auction)

#검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//input[@id="txtKeyword"]')

#search 변수에 저장된 곳에 값을 전송
search.send_keys(word)
search.submit()

res = requests.get(Auction)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
comp1 = soup.find_all("span", attrs={"class":"text--title"})

print("********************** 옥션 가격비교 **********************")
for Auction in comp1:
    title = Auction.a.get_text()
    link = "http://www.auction.co.kr/search?keyword=" + word + Auction.a["href"]   
    print(title, link)
    print()

while True :
    pass
'''


#-*- codingL utf-8 -*- 

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
Coupang = "https://www.coupang.com"
word = input("가격 비교를 할 상품을 입력하세요 : ")

driver = webdriver.Chrome('chromedriver')
driver.get(Coupang)

#검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//input[@id="headerSearchKeyword"]')

#search 변수에 저장된 곳에 값을 전송
search.send_keys(word)
search.submit()

res = requests.get(Coupang)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
comp1 = soup.find_all("div", attrs={"class":"name"})

print("********************** 쿠팡 가격비교 **********************")
for Coupang in comp1:
    title = Coupang.a.get_text()
    link = "https://www.coupang.com/robot.txt" + Coupang.a["href"]   
    print(title, link)
    print()

while True :
    pass




'''
homepage = "https://www.youtube.com/"

word = input("검색어를 입력하세요 : ")

driver = webdriver.Chrome('chromedriver')
driver.get(homepage)

#검색어 창을 찾아 search 변수에 저장
search = driver.find_element_by_xpath('//input[@id="search"]')

#search 변수에 저장된 곳에 값을 전송
search.send_keys(word)
search.submit()

while True :
    pass
'''
