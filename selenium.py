from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from alpacabroker_settings import *

# setting up service and options for driver
ser = Service()

op = webdriver.ChromeOptions()

op.add_experimental_option("debuggerAddress",)

driver = webdriver.Chrome(service = ser, options = op)

driver = webdriver.EdgeOptions()

# dealing with window handles
current_window_handle

window_handles

switch_to.window(driver.window_handles[1])

switch_to.window(driver.window_handles[0])


# finding elements by XPATH
find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/div[1]/div/div/ol/li[last()]/div/div[1]').text

find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div/div[1]').text

find_element(By.XPATH,'//*[@id="market-type-container"]/div[3]/div').text

find_element(By.XPATH,'(//time)[last()]').get_attribute('aria-label')

find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/div[1]/div/div/ol/li[last()]/div/div[1]')

find_element(By.XPATH,'/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[3]/div/main/div[1]/div/div/ol/li[last()]/div/div[1]/div')

find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/div[1]/div/div/ol/li[last()]/div/div[1]').text

find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/div[1]/div/div/ol/li[last()]/div/div[1]').text

find_element(By.XPATH,'//*[@id="market-type-container"]/div[2]/div/div/div[4]').click()

find_element(By.XPATH,'//*[@id="market-type-container"]/div[3]/a/div/button[4]').click()

find_element(By.XPATH,'//*[@id="market-type-container"]/div[3]/div').text

find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/div[1]/div/div/ol/li[last()]/div/div[1]').text

find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[2]/div/main/div[1]/div/div/ol/li[50]/div/div[1]').text

find_element(By.XPATH,'/html/body/div[2]/div[2]/div/div[1]/div/div/div/div/form/div[2]/div/div[1]/div[2]/button[2]').click()

find_elements(By.XPATH, '//*[@id="screener-views-table"]/tbody/tr[5]/td/table/tbody/tr')

find_element(By.XPATH,'//*[@id="screener-views-table"]/tbody/tr[5]/td/table/tbody/tr[last()]').text

find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/table/thead/tr/th[4]').click()

find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/table/thead/tr/th[4]').click()

find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div/div/div/table/tbody').text

find_element(By.XPATH,'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[3]/div/main/div[1]/div/div/ol/li[last()]/div/div[1]').text

find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]').text

find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text

find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[3]').text.strip().replace('$','')

find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[6]/span[1]').text

find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[7]/strong[2]').text.split("-")[0].strip().replace('$','')

find_element(By.XPATH,'/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr[1]/td[7]/strong[2]').text.split("-")[1].strip().replace('$','')

find_element(By.XPATH,'login_box__submit').click()

find_element(By.XPATH,'//*[@id="form-login"]/div/button').click()

find_element(By.XPATH, '//*[@id="app"]/main/div/div[2]/div/div/div[2]/div[1]/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div/div').text

find_element(By.XPATH, '//*[@id="screener-views-table"]/tbody/tr[5]/td/table/tbody/tr[last()]').text

find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[1]/div[3]/div[2]/div[1]/div/table/tbody/tr')

find_elements(By.XPATH, '//*[@id="js-screener-container"]/div[2]/div[1]')

find_elements(By.XPATH, '//*[@id="js-screener-container"]/div[1]')

# finding elements by Class Name
find_element(By.CLASS_NAME,'scroller-kQBbkU').send_keys(Keys.END).scrollBy(0,10000)

find_element(By.CLASS_NAME,'login_box__submit').click()

find_element(By.CLASS_NAME, 'popupModal_button').click()

# finding elements by ID
find_element(By.ID, 'inputEmail').send_keys('hgeitnermitch@gmail.com')

find_element(By.ID,'userid').send_keys('hgeitnermitch')

find_element(By.ID,'inputPassword').send_keys('5xd9rwb8')

find_element(By.ID,'password').send_keys('5xd9rwb8')



