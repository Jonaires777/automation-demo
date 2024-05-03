from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://lambdatest.github.io/sample-todo-app/")
driver.set_window_size(1400, 771)
driver.find_element(By.NAME, "li1").click()
driver.find_element(By.NAME, "li4").click()
driver.find_element(By.ID, "sampletodotext").click()
driver.find_element(By.ID, "sampletodotext").send_keys("Drink water")
driver.find_element(By.ID, "addbutton").click()
driver.find_element(By.ID, "sampletodotext").click()
driver.find_element(By.ID, "sampletodotext").send_keys("meeting with robert")
driver.find_element(By.ID, "addbutton").click()
element = driver.find_element(By.ID, "addbutton")
driver.find_element(By.NAME, "li6").click()
driver.find_element(By.NAME, "li7").click()
driver.find_element(By.NAME, "li2").click()
driver.find_element(By.NAME, "li3").click()
driver.find_element(By.NAME, "li5").click()
driver.quit()