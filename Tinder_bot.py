from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from secrets import u1,p1
d1=webdriver.Edge(executable_path="C:\Windows\System32\WEBDRIVER\msedgedriver.exe")

d1.get("https://tinder.com")
time.sleep(2)

## XPATH FOR TINDER GOLD NO THANKS "//*[@id="modal-manager"]/div/div/div[2]/button[2]/span"

##<span class="Pos(r) Z(1)">No Thanks</span>

## "//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]/span/svg/path"  HEART CLICK

##//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]/span/svg
## "//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]/span/svg"  CROSS CLICK

##d1.find_element_by_xpath("//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]/span/svg")


##d1.current_url



d1.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/div[2]/button/span").click()
time.sleep(5)
base_window=d1.window_handles[0]
#pop_up=d1.window_handles[1]
#inside fb login page
d1.switch_to_window(d1.window_handles[1]) 
email=d1.find_element_by_name("email")
email.send_keys(u1) 

password=d1.find_element_by_name("pass")
password.send_keys(p1) 

d1.find_element_by_xpath("//*[@id='u_0_0']").click()
time.sleep(2)
d1.switch_to_window(d1.window_handles[0])
time.sleep(1)
#d1.find_element_by_xpath("//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span")
d1.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]/span").click()
time.sleep(2)
d1.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]/span").click()
#d1.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]")
##error in this line
#d1.find_element_by_xpath("//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]/span/svg")
time.sleep(4)

like=d1.find_element_by_xpath("//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]")  
like.click()
like.click()
time.sleep(0.5)
like.click()
like.click()
time.sleep(0.5)
like.click()
like.click()
like.click()



