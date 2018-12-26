#!user/bin/python
# coding:utf-8
import requests
from selenium import webdriver
import time
class sdk_bing():
    url="https://cn.bing.com/"
    driver=webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.save_screenshot("bing.png")
    time.sleep(3)
