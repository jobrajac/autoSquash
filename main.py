from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

bane = 3  # 1/2/3
tider = ['2020-12-07 13:30:00', '2020-12-07 14:00:00', '2020-12-07 14:30:00']  # 'yyyy-mm-dd hh:mm:ss'


browser = webdriver.Chrome()
browser.get(('https://www.sit.no/user'))
print("pls logg inn")

while datetime.now().hour < 21:
    time.sleep(5)

browser.get(('https://www.sit.no/trening/squash'))
WebDriverWait(browser, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "ibooking-iframe")))
browser.implicitly_wait(10)

for tid in tider:
    time = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@data-from='"+tid+"']["+str(bane)+"]/a")))
    time.click()
    book = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ScheduleApp"]/div/div/div[5]/div/div/div[2]/div[3]/button')))
    book.click()
    ok = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ModalDiv"]/div/div/div[2]/button')))
    ok.click()
