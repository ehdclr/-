from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import os
from django.test import TestCase




class MyTest(TestCase):
    def setUp(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_argument(f'User-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')
        self.chrome_options.add_argument("lang=ko_KR")
        self.driver = webdriver.Chrome('D:\chromedriver_win32\chromedriver.exe', chrome_options=self.chrome_options)

    def test_2(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('', self.driver.title)

    def tearDown(self) -> None:
        self.driver.quit()




