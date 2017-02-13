# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url='http://umms.reksoft.ru/umms-test/registration/livingLocalRegistration.jsf?navigation=main%2Fregistration&outcome=%2Fregistration%2Findex&registrationCaseType=restrict')
browser.find_element_by_id('usernameInput:username').send_keys('')
browser.find_element_by_id('passwordInput:password').send_keys('')
browser.find_element_by_id('doLogin').click()
browser.find_element_by_id('declarantPerson:docNumberSearchField:text').send_keys('604536')
browser.find_element_by_id('declarantPerson:searchByDocumentDataButton').click()
time.sleep(2)
browser.find_element_by_id('declarantPerson:pddSearchResultTable_data').click()
browser.find_element_by_id('declarantPerson:selectSearchResultButton').click()
time.sleep(2)
browser.find_element_by_id('currentAddress:city:text').send_keys('г Санкт-Петербург')
time.sleep(2)
browser.find_element_by_class_name('ui-autocomplete ui-menu ui-widget ui-widget-content ui-corner-all')

# browser.close()
# time.sleep(30000)
# browser.quit()
