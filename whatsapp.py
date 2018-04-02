from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
a=True
name="Arpit jain excise"
#name="Arpit jain excise"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
print("Chrome open")
assert "WhatsApp" in driver.title
print("Title check")
element = WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[title='Search or start new chat']")))
driver.find_element_by_tag_name("input").send_keys("Arpit jain excise")
print("Entering "+name+" in search")
driver.implicitly_wait(10)
driver.find_element_by_css_selector("span[title='Arpit jain excise']").click()
print("clicking on "+name)
driver.implicitly_wait(10)
blue_tick=driver.find_elements_by_css_selector("span[data-icon='msg-dblcheck-ack']")
blue_tick_count=len(blue_tick)
print("Blue tick count "+str(blue_tick_count))
double_tick=driver.find_elements_by_css_selector("span[data-icon='msg-dblcheck']")
double_tick_count=len(double_tick)
print("Double tick count "+str(double_tick_count))
while a:
    print("starting online check")
    try:
        element = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR,"span[title='online']")))
        print("Online Detected")
        driver.find_element_by_css_selector("span[title='Arpit jain excise']").click()
        driver.switch_to.active_element.send_keys("you are online... :)")
        driver.switch_to.active_element.send_keys('\ue007')
        a=False
    except:
        try:
            driver.switch_to.active_element.send_keys("hi")
            driver.switch_to.active_element.send_keys('\ue007')
            driver.implicitly_wait(5)
            blue_tick=driver.find_elements_by_css_selector("span[data-icon='msg-dblcheck-ack']")
            blue_tick_count1=len(blue_tick)
            double_tick=driver.find_elements_by_css_selector("span[data-icon='msg-dblcheck']")
            double_tick_count1=len(double_tick)
            print("Blue tick count1 "+str(blue_tick_count1))
            print("Double tick count1 "+str(double_tick_count1))
            if blue_tick_count1!=blue_tick_count or double_tick_count1!=double_tick_count:
                driver.switch_to.active_element.send_keys("Welcome online.... :)")
                driver.switch_to.active_element.send_keys('\ue007')
                a=False
        except:
            print("something wrong with codes")
driver.quit()

