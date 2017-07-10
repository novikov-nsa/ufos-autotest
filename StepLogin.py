from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get("http://depr-dev-jetty.otr.ru:28080/")

def waitElementXpath(x, timer=20):
    WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.XPATH, x)))

def waitElementID(x, timer=20):
    WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.ID, x)))

def waitElementName(x, timer=20):
    WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.NAME, x)))

waitElementID("user")

driver.find_element_by_id("user").clear()
driver.find_element_by_id("user").send_keys("aa_petrov")
driver.find_element_by_id("psw").clear()
driver.find_element_by_id("psw").send_keys("voda1")
driver.find_element_by_id("okButton").click()

waitElementXpath("//tr[@class='navigation-treerow-first z-treerow'][@title='Документы']")
elemNavigation = driver.find_element_by_xpath("//tr[@class='navigation-treerow-first z-treerow'][@title='Документы']")
elemNavigation.click()

waitElementXpath("//tr[@class='z-treerow'][@title='Заявление об установлении (изменении) тарифа']")
elemNavigation = driver.find_element_by_xpath("//tr[@class='z-treerow'][@title='Заявление об установлении (изменении) тарифа']")
elemNavigation.click()

waitElementXpath("//tr[@class='z-treerow'][@title='Все']")
elemNavigation = driver.find_element_by_xpath("//tr[@class='z-treerow'][@title='Все']")
elemNavigation.click()

waitElementXpath("//button[@title='Создать новый документ']")
ButtonBar = driver.find_element_by_xpath("//button[@title='Создать новый документ']")
ButtonBar.click()


waitElementName("efl_doc_inf_typerequest")
driver.find_element_by_name("efl_doc_inf_typerequest").click()

waitElementXpath("//span[@class='z-comboitem-text']")
driver.find_element_by_xpath("//span[@class='z-comboitem-text']").click()


waitElementXpath("//button[text()='Добавить основание']")
driver.find_element_by_xpath("//button[text()='Добавить основание']").click()



waitElementXpath("//div[@class='z-listcell-content'][text()='Федеральный закон от 07.12.2011 N 416-ФЗ (ред. от']")
elem = driver.find_element_by_xpath("//div[@class='z-listcell-content'][text()='Федеральный закон от 07.12.2011 N 416-ФЗ (ред. от']")
ActionChains(driver).move_to_element(elem).click(elem).perform()

waitElementXpath("//button[text()='OK']")
driver.find_element_by_xpath("//button[text()='OK']").click()


waitElementXpath("//span[text()='Заявитель']/parent::a/parent::li[@class='z-tab']")
driver.find_element_by_xpath("//span[text()='Заявитель']").click()


waitElementXpath("//input[@name='chb_doc_org_checkinfo']/following-sibling::div")
elem = driver.find_element_by_xpath("//input[@name='chb_doc_org_checkinfo']/following-sibling::div")
ActionChains(driver).move_to_element(elem).click(elem).perform()



waitElementXpath("//span[text()='Тарифы и зоны']/parent::a/parent::li[@class='z-tab']")
driver.find_element_by_xpath("//span[text()='Тарифы и зоны']").click()

waitElementXpath("//button[@title='Выбрать из справочника']")
driver.find_element_by_xpath("//button[@title='Выбрать из справочника']").click()


waitElementXpath("//div[@class='z-listcell-content'][text()='Водоснабжение и водоотведение']")
elem = driver.find_element_by_xpath("//div[@class='z-listcell-content'][text()='Водоснабжение и водоотведение']")
ActionChains(driver).move_to_element(elem).click(elem).perform()


waitElementXpath("//button[text()='OK'][@class='acceptButton z-button']")
driver.find_element_by_xpath("//button[text()='OK'][@class='acceptButton z-button']").click()



ButtonBar = driver.find_element_by_xpath("//button[@title='Сохранить изменения и закрыть окно']")
ButtonBar.click()



x=1





