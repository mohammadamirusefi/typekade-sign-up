from selenium import webdriver
import time
from selenium .webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://typekadeh.com")
btns=driver.find_elements(By.XPATH,'//*[@id="__nuxt"]/div/div/header/div/div/div[3]/button')
btn=btns[0]
btn.click()
time.sleep(1)
sign=driver.find_elements(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[1]/form/div[2]')
sgn=sign[0]
sgn.click()
time.sleep(1)
email=driver.find_elements(By.XPATH,'//*[@id="__nuxt"]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[1]/div/input')
gmail=email[0]
gmail.send_keys("random@gmail.com")
time.sleep(1)
name=driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[2]/div/input')
esm=name[0]
esm.send_keys("randomname1")
time.sleep(1)
password=driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[3]/div/input')
pw=password[0]
pw.send_keys("PASSWORD")
ending=driver.find_elements(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/transition/div/div[2]/div/div/div/div[2]/div/div[2]/form/div/div[4]/div/button')
end=ending[0]
end.click()
time.sleep(10)