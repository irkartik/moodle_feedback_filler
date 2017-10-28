from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

driver = webdriver.Chrome('/home/raj/Desktop/autosend-whatsapp/chromedriver')

driver.get("http://moodle.msit.in/login/index.php")
wait = WebDriverWait(driver, 100)

driver.execute_script("document.querySelectorAll('div.textbox-wrap > input')[0].value='6115002715'")
driver.execute_script("document.querySelectorAll('div.textbox-wrap > input')[1].value='Moodle@31'")

login_xpath = '//input[contains(@id, "loginbtn1")]'
login = wait.until(EC.presence_of_element_located((By.XPATH, login_xpath)))
login.click()

feedback_link_xpath = '//a[contains(@href, "http://moodle.msit.in/course/view.php?id=693")]'
feedback_link = wait.until(EC.presence_of_element_located((By.XPATH, feedback_link_xpath)))
feedback_link.click()

ada_theory = 9345
se_theory = 9346
java_theory = 9347
im_theory = 9348
dcs_theory = 9349
cs_theory = 9351 

ada_lab_code_A_B = 9352
ada_lab_code_C = 9354
se_lab_A = 5355
se_lab_B_C = 9356
java_lab = 9357
dcs_lab = 9359
cs_lab = 9361 

lab_codes_A = [ada_lab_code_A_B, se_lab_A ,java_lab, dcs_lab, cs_lab]
lab_codes_B = [ada_lab_code_A_B, se_lab_B_C ,java_lab, dcs_lab, cs_lab]
lab_codes_C = [ada_lab_code_C ,se_lab_B_C ,java_lab, dcs_lab, cs_lab]
ada_theory
subject_codes = [se_theory, java_theory, im_theory, dcs_theory, cs_theory]

for code in subject_codes:
	subject_link_xpath = '//a[contains(@href, "http://moodle.msit.in/mod/feedback/view.php?id=' + str(code) + '")]'
	subject_link = wait.until(EC.presence_of_element_located((By.XPATH, subject_link_xpath)))
	subject_link.click()

	try:
		elm = driver.find_element_by_link_text('Answer the questions...')

		if elm.is_displayed():
			print('foo')
			elm.click()

			driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[0].value='50%'")
			driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[1].value='50%'")
			driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[2].value='all good'")
			driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[3].value='all good'")

			for i in range(7):
				driver.execute_script("document.querySelectorAll(\"span.feedback_item_radio_v_left > input[value='2']\")[" + str(i)  + "].checked = true;")

			submit_answer_xpath = "//input[contains(@name, 'savevalues')]"
			submit_answer = wait.until(EC.presence_of_element_located((By.XPATH, submit_answer_xpath)))
			submit_answer.click()
		else:
			continue
		print('hello')
	except NoSuchElementException:
		print('no element found')
	if driver.execute_script("document.querySelectorAll(\"form > div > input[type='submit']\")[0].click()") != None:
		driver.execute_script("document.querySelectorAll(\"form > div > input[type='submit']\")[0].click()")

"""
IN THE FOR LOOP BELOW REPLACE THE <LAB CODE HERE> WITH THE FOLLOWING CODES:
1. lab_codes_A : IF YOU BELONG TO GROUP A
2. lab_codes_B : IF YOU BELONG TO GROUP B
3. lab_codes_C : IF YOU BELONG TO GROUP C
"""
for code in lab_codes_B:
	subject_link_xpath = '//a[contains(@href, "http://moodle.msit.in/mod/feedback/view.php?id=' + str(code) + '")]'
	subject_link = wait.until(EC.presence_of_element_located((By.XPATH, subject_link_xpath)))
	subject_link.click()

	try:
		elm1 = driver.find_element_by_link_text('Answer the questions...')
		if elm1.is_displayed():
			elm1.click()
			try:
				driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[0].value='50%'")
				driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[1].value='80%'")
				driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[2].value='yes'")
				driver.execute_script("document.querySelectorAll('span.feedback_item_textfield > input')[3].value='all good'")

				for i in range(5):
					driver.execute_script("document.querySelectorAll(\"span.feedback_item_radio_v_left > input[value='2']\")[" + str(i)  + "].checked = true;")

				driver.execute_script("document.querySelectorAll(\"span.feedback_item_radio_v_left > input[value='1']\")[5].checked = true;")

				submit_answer_xpath = "//input[contains(@name, 'savevalues')]"
				submit_answer = wait.until(EC.presence_of_element_located((By.XPATH, submit_answer_xpath)))
				submit_answer.click()
			except WebDriverException:
				print('no form')
				cancel_button = driver.find_element_by_link_text('Cancel')
				cancel_button.click()


		else: 
			continue
	except NoSuchElementException:
			print('no element found')
	try:
		driver.execute_script("document.querySelectorAll(\"form > div > input[type='submit']\")[0].click()")
	except:
		try:
			continue_button = driver.find_element_by_link_text('Continue the form')
			if continue_button.is_displayed():
				continue_button.click()
		except:
				cancel_button = driver.find_element_by_tag_name('button')
				cancel_button.click()
		
		#driver.execute_script("document.querySelectorAll(\"form > div > input[type='submit']\")[0].click()")
