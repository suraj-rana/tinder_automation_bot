from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from secrets import user_name,pass_word
# giving path directory to webdriver location and also change your browser for example i am using Edge so i use webdriver.Edge() similarly you can use chrome etc.
web_window=webdriver.Edge(executable_path="C:\Windows\System32\WEBDRIVER\msedgedriver.exe")

web_window.get("https://tinder.com/")
time.sleep(5)
#print(web_window.title)
#assert "Tinder | Match. Chat. Date." in web_window.title
class NoSuchElementException(Exception):
    """element not found"""
    pass
class new_popup_found(Exception):
    """unwanted popup appeared"""
    pass  
try:
    if(bool(web_window.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/div[2]/button/span[2]")))==False:
        raise NoSuchElementException
    else:
        web_window.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/div[2]/button/span[2]").click()
except NoSuchElementException:
    time.sleep(2)
    web_window.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/div[2]/button/span[2]").click()


old=web_window.window_handles[0]
time.sleep(2)
#changing webdriver object to popup window and viceversa
new=web_window.switch_to_window(web_window.window_handles[1])

web_window.find_element_by_xpath("//*[@id='email']").send_keys(user_name)  # put user_name in secrets.py
web_window.find_element_by_xpath("//*[@id='pass']").send_keys(pass_word)  ## put pass_word in secrets.py
web_window.find_element_by_xpath("//*[@id='u_0_0']").click()

time.sleep(2)
web_window.switch_to_window(web_window.window_handles[0])  #swithing webdriver to default window
time.sleep(1)

web_window.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]/span").click() #enable loation
time.sleep(2)
web_window.find_element_by_xpath("//*[@id='modal-manager']/div/div/div/div/div[3]/button[1]/span").click() #another popup


time.sleep(4)

like=web_window.find_element_by_xpath("//*[@id='content']/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]")  #like button element
def unwanted_popup():#still working on this function
    try:
        if(bool(web_window.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/button[2]/span")))==True:
            raise new_popup_found
        else:
            pass
    except new_popup_found:
        time.sleep(2)
        web_window.find_element_by_xpath("//*[@id='modal-manager']/div/div/div[2]/button[2]/span").click()
    


while(bool(like)==True): #main action
    like.click()
    time.sleep(0.2)

print("THE END...NOW WAIT FOR MATCH")
    


