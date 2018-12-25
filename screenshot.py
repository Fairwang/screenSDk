#!user/bin/python
# coding:utf-8
import requests
from selenium import webdriver
import time
url="https://cpay.hypayde.com/t_q_code?id=T10251812171057414120"

driver=webdriver.Chrome()
driver.get(url)
time.sleep(3)
driver.save_screenshot("123456.png")
time.sleep(3)
