import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(
    executable_path=r"C:\Frameworks\Python\myseleniumpythonproject\browsers\chromedriver_win32\chromedriver.exe")
driver.get("http://automationpractice.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_link_text("Sign in").click()
time.sleep(3);
driver.find_element_by_id("email").send_keys("gaurav05153@gmail.com")
driver.find_element_by_id("passwd").send_keys("admin")
driver.find_element_by_id("SubmitLogin").click()
time.sleep(3);
'''driver.find_element_by_xpath("//a[@title='Orders']").click()
message = driver.find_element_by_id("block-history").text
assert message in "You have not placed any orders."
'''
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_xpath("//a[@title='Women']")
action.move_to_element(firstLevelMenu).perform()
secondLevelMenu = driver.find_element_by_xpath("//a[@title='T-shirts']")
action.move_to_element(secondLevelMenu).click().perform()
# driver.find_element_by_xpath("//a[@title='Women']").click()
time.sleep(5)

tshirt_path = driver.find_element_by_xpath("//a[@title='Faded Short Sleeve T-shirts']/img")
driver.execute_script("arguments[0].scrollIntoView();", tshirt_path)
time.sleep(2)
action = ActionChains(driver)
action.move_to_element(tshirt_path).perform()
driver.find_element_by_xpath("//a[@title='Add to cart']").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@title='Proceed to checkout']/span").click()
time.sleep(2)
print(driver.title)
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script("window.scrollBy(0,500)","")
requiredCheckoutpath= driver.find_element_by_xpath("//a[@title='Continue shopping']/preceding-sibling::a/span")
requiredCheckoutpath.click()
time.sleep(2)
driver.find_element_by_xpath("//button[@name='processAddress']/span").click()
time.sleep(1)
driver.find_element_by_id("cgv").click()
driver.find_element_by_xpath("//button[@name='processCarrier']/span").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@title='Pay by bank wire']").click()
time.sleep(1)
driver.find_element_by_xpath("//button[@type='submit']/span[text()='I confirm my order']").click()
time.sleep(1)
message1=driver.find_element_by_xpath("//p[@class='cheque-indent']/strong").text
assert message1 in "Your order on My Store is complete."




driver.close()
