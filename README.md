# register on Typekadeh.com with selenium
## we are here for to explain the steps to register on[typekadeh.com](https://typekadeh.com)
## this site is designed to help you improve your typing skills.
### for first we need to install and import the `selenium` package
``` 
pip install selenium
```
``` python
import selenium
``` 
---
### after install selenium package you need to import some modules
``` python
from selenium import webdriver
import time
from selenium .webdriver.common.by import By
```
### We need to do step to open the site
- ``` python
    driver = webdriver.Chrome()
    driver.get("https://typekadeh.com")
---
### We use `XPATH` to continue writing the code and complete it.
the base form of using xpath in this code is:
``` python 
btns=driver.find_elements(By.XPATH,'_____')
```
---
### for end we write:
    time.sleep(100)
###  to make the code work