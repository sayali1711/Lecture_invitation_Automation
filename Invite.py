from selenium import webdriver
import time
#Enter Your path to the chromedriver.exe
driver=webdriver.Chrome("D:\\pycharm_programs\\pycharm projects\\venv\\ChromeDriver\\chromedriver.exe")

#Google Sign-In
driver.get("https://google.com")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="gb"]/div/div[2]/a').click()
time.sleep(4)

#email address
driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('mail_id')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()
time.sleep(4)

#Enter password
driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys("password")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()# Click on next button after entering the password
time.sleep(5)

#Google Meet
driver.get("https://meet.google.com/")
driver.find_element(By.Xpath,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[1]/div/button/span').click()
driver.find_element(By.Xpath,'//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div[1]/div[3]/div/div[1]/div[2]/div/ul/li[2]/span[3]').click()

#camera off
driver.find_element(By.XPATH,'//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[2]/div/span/button/div[2]/div/svg').click()

#mic off
driver.find_element(By.XPATH,'//*[@id="ow3"]/div[1]/div/div[9]/div[3]/div[10]/div[2]/div/div[1]/div/div/span/button/div[2]/div[1]/div/svg/g/g/path').click()
meetId=driver.find_element(By.XPATH,'//*[@id="ow3"]/div[3]/div[2]/div[3]/div[2]/div/span/span/span/svg').click()

#Whatsapp
driver.get("https://web.whatsapp.com/")
input("Scan the QR Code and Press any Key to Continue: ")
grp_name=driver.find_element_by_css_selector('span[title="group_name"]')
grp_name.click();
text_input=driver.find_element_by_xpath('/html/body/div/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div[2]/div/div[2]')
time.sleep(10)
text_input.send_keys('Join meeting using  link given below')
text_input.send_keys(meetId)
text_input.send_keys(Keys.RETURN)

#Gmail the link
driver.get("https://https://mail.google.com/mail/u/0/#inbox")
driver.find_element_by_xpath('//*[@id=":kr"]/div/div').click()
#after compose
driver.find_element_by_xpath('//*[@id=":r2"]').send_keys('email_group_name')
driver.find_element_by_xpath('//*[@id=":qk"]').send_keys('Join this link for the lecture')
driver.find_element_by_xpath('//*[@id=":rp"]').send_keys(meetId)
driver.find_element_by_xpath('//*[@id=":px"]').click()

