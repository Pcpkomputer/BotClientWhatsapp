from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as auto

driver = webdriver.Chrome("D:/chromedriver.exe")
driver.get("http://web.whatsapp.com")
try:
    element = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.CLASS_NAME , "_2bBPp"))
    )
finally:
    print("debug")
    while True:
        time.sleep(1)
        try:
            element = driver.find_elements(By.CLASS_NAME, '_31gEB')
            ez = driver.find_element(By.CLASS_NAME, '_1EFSv')
            ez.click()
            
            x = driver.find_elements(By.CLASS_NAME,"_3FRCZ")[1]
            x.click()
          
            for x in element:
                time.sleep(1)
                x.click()
                element = WebDriverWait(driver, 60).until(
                    EC.presence_of_element_located((By.CLASS_NAME , "message-in"))
                )
                pop = driver.find_elements(By.CLASS_NAME, 'message-in')
                ele = pop[len(pop)-1].find_element(By.CLASS_NAME, "eRacY")
                ew = ele.find_elements(By.TAG_NAME,"span")[1]
                print(ew.get_attribute("innerText"))
                auto.write("asdkasodksakdsad")
                auto.press("enter")
        except Exception as e:
            print(e)
            pass
        

    
