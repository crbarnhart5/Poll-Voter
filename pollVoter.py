from selenium import webdriver
import time, sys
num = int(input('Please enter the amount of times you would like to vote: '))
for i in range(1, num+1):
    browser = webdriver.Firefox()
    browser.get('https://goo.gl/UcNyM4')
    button = browser.find_element_by_name('qp_v854840')
    button.click()
    vote = browser.find_element_by_name('qp_b854840')
    vote.click()
sys.exit()
    
