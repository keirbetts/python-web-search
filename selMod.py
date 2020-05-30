from selenium import webdriver


chromedriver = "./chromedriver 2"
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.google.com/')

searchElem = browser.find_element_by_css_selector(
    '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input')

searchElem.send_keys('rabbits')
searchElem.submit()


# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()


# elem.click()

# elems = browser.find_elements_by_css_selector('p')
# print(len(elems))

elem = browser.find_element_by_css_selector('#gsr')

print(elem.text)

# See below to get all text on web page

# elem = browser.find_element_by_css_selector('html')

# elem.text
