from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

class Operation(object):
    def toExecute(self,setOperation):
        nameOperation = setOperation[0]
        typeOperation = setOperation[1]
        print(nameOperation,typeOperation)
        resaultOperation = 'Начало выполнения'

        if typeOperation=='Зайти под пользователем':
            Operation().opLogin(setOperation)
            resaultOperation = 'Ок'

        if typeOperation=='Открыть в меню навигации':
            Operation().opMenuNavigator(setOperation)
            resaultOperation = 'Ок'

        if typeOperation=='Кнопка на скроллере':
            Operation().opKeyScroller(setOperation)
            resaultOperation = 'Ок'

        if typeOperation=='Выбрать из списка':
            Operation().opSetlListBox(setOperation)
            resaultOperation = 'Ок'

        if typeOperation=='Выбрать из справочника':
            Operation().opSetDict(setOperation)
            resaultOperation = 'Ок'

        if typeOperation=='Перейти на закладку':
            Operation().opGoToTabPanel(setOperation)
            resaultOperation = 'Ок'

        if typeOperation=='Установить чекер':
            Operation().opCheckTrue(setOperation)
            resaultOperation = 'Ок'


        return resaultOperation


    def opLogin(self,setOperation):
    # Операция "Зайти под пользователем"
    # Возможные параметры
    # Логин,Пароль

    # Выставить параметры
        for itemParam in setOperation:
            spParam=itemParam.split('=')
            nameParam=spParam[0]
            if nameParam == 'Логин': userLogin = spParam[1]
            if nameParam == 'Пароль': userPassword = spParam[1]

    #Открыть в браузере
        driver.get("http://depr-dev-jetty.otr.ru:28080/")

    #Ожидание появления поля
        waitElementID("user")
    #Ввод значения
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys(userLogin)
        driver.find_element_by_id("psw").clear()
        driver.find_element_by_id("psw").send_keys(userPassword)
        driver.find_element_by_id("okButton").click()

    def opMenuNavigator(self,setOperation):
        # Операция "Открыть в меню навигации"
        # Возможные параметры
        # Путь (Задается через разделитель / знак * означает корневой элемент)

        # Выставить параметры
        for itemParam in setOperation:
            spParam = itemParam.split('=')
            nameParam = spParam[0]
            if nameParam == 'Путь': menuStr = spParam[1]

        for menuItem in menuStr.split('/'):
            if menuItem[0]=='*':
                xpathSt = "//tr[@class='navigation-treerow-first z-treerow'][@title='" + menuItem[1:] + "']"

            if menuItem[0]!='*':
                xpathSt = "//tr[@class='z-treerow'][@title='" + menuItem + "']"

            waitElementXpath(xpathSt)
            elemNavigation = driver.find_element_by_xpath(xpathSt)
            elemNavigation.click()

    def opKeyScroller(self,setOperation):
    # Операция "Кнопка на скроллере"
    # Возможные параметры
    # Название

    # Выставить параметры
        for itemParam in setOperation:
            spParam=itemParam.split('=')
            nameParam=spParam[0]
            if nameParam == 'Название': keyName = spParam[1]

        xpathSt="//button[@title='" + keyName + "']"
        waitElementXpath(xpathSt)
        driver.find_element_by_xpath(xpathSt).click()


    def opSetlListBox(self,setOperation):
    # Операция "Выбрать из списка"
    # Возможные параметры
    # Название

    # Выставить параметры
        for itemParam in setOperation:
            spParam=itemParam.split('=')
            nameParam=spParam[0]
            if nameParam == 'Системное имя кнопки': sysKeyName = spParam[1]
            if nameParam == 'Выбрать': selType = spParam[1]

        #Нажать кнопку выбора
        xpathSt = sysKeyName
        waitElementName(xpathSt)
        driver.find_element_by_name(xpathSt).click()

        #Выбрать первый попавшийся элемент
        waitElementXpath("//span[@class='z-comboitem-text']")
        driver.find_element_by_xpath("//span[@class='z-comboitem-text']").click()

    def opSetDict(self,setOperation):
    # Операция "Выбрать из справочника"
    # Возможные параметры
    # Название кнопки
    # Значение (может принимать = , =~ )

    # Выставить параметры
        for itemParam in setOperation:
            spParam=itemParam.split('=')
            nameParam=spParam[0]
            if nameParam == 'Название кнопки':
                sysKeyName = spParam[1]
                xpathSt = "//button[text()='" + sysKeyName + "']"
            if nameParam == 'Подсказка на кнопке':
                sysKeyName = spParam[1]
                xpathSt = "//button[@title='" + sysKeyName + "']"

            if nameParam == 'Значение':
                dictValue = spParam[1]
                xpathStDict = "//div[@class='z-listcell-content'][text()='" + dictValue + "']"
                if dictValue[0] == '~': xpathStDict = "//div[@class='z-listcell-content'][contains(text(), '" + dictValue[1:] + "')]"


        waitElementXpath(xpathSt)
        driver.find_element_by_xpath(xpathSt).click()

        #print(xpathStDict)

        if dictValue != 'Выбрать любое значение':
            waitElementXpath(xpathStDict)
            elem = driver.find_element_by_xpath(xpathStDict)
            ActionChains(driver).move_to_element(elem).click(elem).perform()

        if dictValue == 'Выбрать любое значение':
            # Не работает
            waitElementXpath(xpathStDict)
            elem = driver.find_element_by_xpath(xpathStDict)
            ActionChains(driver).move_to_element(elem).click(elem).perform()


        waitElementXpath("//button[text()='OK']")
        driver.find_element_by_xpath("//button[text()='OK']").click()


    def opGoToTabPanel(self,setOperation):
    # Операция "Перейти на закладку"
    # Возможные параметры
    # Название
    # Значение (может принимать = , =~ )

    # Выставить параметры
        for itemParam in setOperation:
            spParam = itemParam.split('=')
            nameParam = spParam[0]
            if nameParam == 'Название': panName = spParam[1]
            if nameParam == 'Пауза': pauseVal = spParam[1]

        xpathSt = "//span[text()='" + panName + "']/parent::a/parent::li[@class='z-tab']"
        xpathSt2 = "//span[text()='" + panName + "']"

        print(xpathSt2)
        waitElementXpath(xpathSt)
        waitElementXpath(xpathSt2)
        elem = driver.find_element_by_xpath(xpathSt2)
        ActionChains(driver).move_to_element(elem).click(elem).perform()

    def opCheckTrue(self,setOperation):
    # Операция "Установить чекер"
    # Возможные параметры
    # Системное имя

    # Выставить параметры
        for itemParam in setOperation:
            spParam = itemParam.split('=')
            nameParam = spParam[0]
            if nameParam == 'Системное имя': elemName = spParam[1]
            if nameParam == 'Пауза': pauseVal = spParam[1]

        xpathSt = "//input[@name='" + elemName + "']/following-sibling::div"

        waitElementXpath(xpathSt)
        elem = driver.find_element_by_xpath(xpathSt)
        ActionChains(driver).move_to_element(elem).click(elem).perform()


    pass


def waitElementXpath(x, timer=60):
    WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.XPATH, x)))

def waitElementID(x, timer=60):
    WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.ID, x)))

def waitElementName(x, timer=60):
    WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.NAME, x)))