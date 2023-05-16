# Import Selenium Webdriver,XPATH modules
from selenium import webdriver

from selenium.webdriver.common.by import By

# import Time
import time

# Initialize the webdriver
driver = webdriver.Chrome()

driver.maximize_window()


# Navigate to the Page
print("-------- opening web application ----------")

driver.get("http://127.0.0.1:5000")

print("-------- web application opened ----------")

print("-------- inputting user credentials -----------")

time.sleep(4)

username = driver.find_element("id", "username")

username.send_keys('test')

time.sleep(2)

password = driver.find_element("id", "password")

password.send_keys('tests')

time.sleep(2)



print("---------user credentials inputted---------")

# This tells python to wait for 3 seconds before continuing the test
time.sleep(3)

print("--------clicked to authenticate user AD-----------")

driver.find_element(By.XPATH, "/html/body/div/form/input[4]").click()

print("---------user signed in successful------------")

# This tells python to wait for 12 seconds before continuing the test
#time.sleep(2)

time.sleep(4)

user_name = driver.find_element("id", "username")

user_name.send_keys('test')

time.sleep(2)

pass_word = driver.find_element("id", "password")

pass_word.send_keys('test')

time.sleep(2)

driver.find_element(By.XPATH, "/html/body/div/form/input[4]").click()


print("----------checking if user was redirected---------")

signed_in = driver.find_element(By.XPATH, '/html/body/h1').text

time.sleep(2)

print(signed_in)

if signed_in == "WELCOME":

    print("-- login successful --")

    print("-----------user redirected-----------------")

else:

    print('---- log in failed-----')

time.sleep(3)

print("---------- PLEASE WAIT:entering required user data-------")

firstname = driver.find_element("id", "firstname")

firstname.send_keys("Richard")

time.sleep(2)

middle_name = driver.find_element("id", "middlename")

middle_name.send_keys("Agyemang")

time.sleep(2)

surname = driver.find_element("id", "surname")

surname.send_keys("Darkwah")

time.sleep(2)

othernames = driver.find_element("id", "othernames")

othernames.send_keys("Miles")

time.sleep(2)

nationality = driver.find_element("id", "nationality")

nationality.send_keys("Ghanaian")

time.sleep(2)

placeofbirth = driver.find_element("id", "placeofbirth")

placeofbirth.send_keys("Sweden")

time.sleep(2)

Contact = driver.find_element("id", "contact")

Contact.send_keys("024325647")

time.sleep(2)

address = driver.find_element("id", "address")

address.send_keys("Stockholm")

time.sleep(2)

eaddress = driver.find_element("id", "eaddress")

eaddress.send_keys("TEST@cbg.com")

time.sleep(2)

city = driver.find_element("id", "city")

city.send_keys("Paris")

time.sleep(2)

print("------- user data entry:COMPLETE --------")

time.sleep(4)

driver.find_element(By.XPATH, "/html/body/div/form/input[11]").click()

print("-----submitting Form-----------")

time.sleep(5)


# Close the webdriver
driver.close()

print("--------automation DONE ----------")