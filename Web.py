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

        if typeOperation == 'Зайти под пользователем':              resaultOperation = Operation().opLogin(setOperation)
        if typeOperation == 'Открыть в меню навигации':             resaultOperation = Operation().opMenuNavigator(setOperation)
        if typeOperation == 'Кнопка на скроллере':                  resaultOperation = Operation().opKeyScroller(setOperation)
        if typeOperation == 'Выбрать из списка':                    resaultOperation = Operation().opSetlListBox(setOperation)
        if typeOperation == 'Выбрать из справочника':               resaultOperation = Operation().opSetDict(setOperation)
        if typeOperation == 'Перейти на закладку':                  resaultOperation = Operation().opGoToTabPanel(setOperation)
        if typeOperation == 'Установить чекер':                     resaultOperation = Operation().opCheckTrue(setOperation)
        if typeOperation == 'Установить радио кнопку':              resaultOperation = Operation().opCheckRadioBut(setOperation)
        if typeOperation == 'Нажать кнопку':                        resaultOperation = Operation().opButton(setOperation)
        if typeOperation == 'Сохранить изменения и закрыть окно':   resaultOperation = Operation().opButtonSaveAndClose(setOperation)
        if typeOperation == 'Сохранить изменения':                  resaultOperation = Operation().opButtonSave(setOperation)

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
        waitElement("user", reqType='ID')

    #Ввод значения
        driver.find_element_by_id("user").clear()
        driver.find_element_by_id("user").send_keys(userLogin)
        driver.find_element_by_id("psw").clear()
        driver.find_element_by_id("psw").send_keys(userPassword)
        driver.find_element_by_id("okButton").click()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation

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

            waitElement(xpathSt)
            elemNavigation = driver.find_element_by_xpath(xpathSt)
            elemNavigation.click()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation

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
        waitElement(xpathSt)
        driver.find_element_by_xpath(xpathSt).click()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation


    def opSetlListBox(self,setOperation):
    # Операция "Выбрать из списка"
    # Возможные параметры
    # Название

    # Выставить параметры
        for itemParam in setOperation:
            spParam=itemParam.split('=')
            nameParam=spParam[0]
            if nameParam == 'Системное имя кнопки': sysKeyName = spParam[1]
            if nameParam == 'Выбрать': selValue = spParam[1]

        #Нажать кнопку выбора
        xpathSt = sysKeyName
        #waitElementName(xpathSt)
        waitElement(xpathSt, reqType='NAME')
        driver.find_element_by_name(xpathSt).click()

        #Выбрать первый попавшийся элемент

        xpathList = "//span[@class='z-comboitem-text'][contains(text(), '" + selValue + "')]"
        waitElement(xpathList)
        driver.find_element_by_xpath(xpathList).click()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation

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


        waitElement(xpathSt)
        driver.find_element_by_xpath(xpathSt).click()

        #print(xpathStDict)

        if dictValue != 'Выбрать любое значение':
            waitElement(xpathStDict)
            elem = driver.find_element_by_xpath(xpathStDict)
            ActionChains(driver).move_to_element(elem).click(elem).perform()

        if dictValue == 'Выбрать любое значение':
            # Не работает
            waitElement(xpathStDict)
            elem = driver.find_element_by_xpath(xpathStDict)
            ActionChains(driver).move_to_element(elem).click(elem).perform()


        waitElement("//button[text()='OK']")
        driver.find_element_by_xpath("//button[text()='OK']").click()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation

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

        waitElement(xpathSt)
        waitElement(xpathSt2)
        elem = driver.find_element_by_xpath(xpathSt2)
        ActionChains(driver).move_to_element(elem).click(elem).perform()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation

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

        waitElement(xpathSt)
        elem = driver.find_element_by_xpath(xpathSt)
        ActionChains(driver).move_to_element(elem).click(elem).perform()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation


    def opCheckRadioBut(self,setOperation):
    # Операция "Установить радио кнопку"
    # Возможные параметры
    # Системное имя

    # Выставить параметры
        for itemParam in setOperation:
            spParam = itemParam.split('=')
            nameParam = spParam[0]
            if nameParam == 'Значение': elemValue = spParam[1]
            if nameParam == 'Пауза': pauseVal = spParam[1]

        xpathSt = "//label[text()='" + elemValue + "'][@class='z-advradio-content']"

        waitElement(xpathSt)
        elem = driver.find_element_by_xpath(xpathSt)
        ActionChains(driver).move_to_element(elem).click(elem).perform()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation


    def opButton(self,setOperation):
    # Операция "Кнопка"
    # Возможные параметры
    # Название

    # Выставить параметры
        elemPos = '1'
        for itemParam in setOperation:
            spParam=itemParam.split('=')
            nameParam=spParam[0]
            if nameParam == 'Название': keyName = spParam[1]
            if nameParam == 'Порядок': elemPos = spParam[1]

        xpathSt = "//button[text()='" + keyName + "'][" + elemPos + "]"
        waitElement(xpathSt)
        #driver.find_element_by_xpath(xpathSt).click()

        element = driver.find_element_by_xpath(xpathSt)
        ActionChains(driver).move_to_element(element).click(element).perform()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation

    def opButtonSaveAndClose(self,setOperation):
    # Операция "Кнопка"
    # Возможные параметры
    # Название

    # Выставить параметры
        posKey = '1'
        for itemParam in setOperation:
            spParam=itemParam.split('=')
            nameParam=spParam[0]
            if nameParam == 'Дочерний документ': posKey = '2'

        xpathSt="//button[@title='Сохранить изменения и закрыть окно']"

        #xpathSt = "//button[@title='Сохранить изменения и закрыть окно'][1]"

        waitElement(xpathSt)

        element = driver.find_elements_by_xpath(xpathSt)
        #ActionChains(driver).move_to_element(element).click(element).perform()
        if posKey == '1': ActionChains(driver).move_to_element(element).click(element).perform()
        if posKey == '2': ActionChains(driver).move_to_element(element[1]).click(element[1]).perform()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation

    def opButtonSave(self, setOperation):
        # Операция "Кнопка"
        # Возможные параметры
        # Название

        # Выставить параметры
        posKey = '1'
        for itemParam in setOperation:
            spParam = itemParam.split('=')
            nameParam = spParam[0]
            if nameParam == 'Дочерний документ': posKey = '2'

        xpathSt = "//button[@title='Сохранить изменения']"

        # xpathSt = "//button[@title='Сохранить изменения и закрыть окно'][1]"

        waitElement(xpathSt)

        element = driver.find_elements_by_xpath(xpathSt)
        # ActionChains(driver).move_to_element(element).click(element).perform()
        if posKey == '1': driver.find_element_by_xpath(xpathSt).click()
        if posKey == '2': ActionChains(driver).move_to_element(element[1]).click(element[1]).perform()

        resaultOperation = '[Операция выполнена -] ' + setOperation[1]
        return resaultOperation





    pass



def waitElement(reqText, reqType='XPATH',timer=60 ,typeSearch = 'presence_of_element_located'):
#Проверка наличия индикатора ожидания обработки страницы
#Если найден элемент //div[@class='z-loading-indicator'] ожидаем 60 сек. пока он пропадет
    try:
        WebDriverWait(driver, 1.1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='z-loading-indicator']")))
    except Exception: x=1
    else:
        for i in range(60):
            try:
                time.sleep(1)
                WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='z-loading-indicator']")))
            except Exception: break
            else: print("[Ожидание обработки страницы ]", i, "сек")
        if i==60:
            print("[error] Превышено время ожидания")
            exit(10)

#Проверяем наличие элемента
    try:
        if typeSearch == 'presence_of_element_located':
            if reqType == 'XPATH': WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.XPATH, reqText)))
            if reqType == 'ID': WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.ID, reqText)))
            if reqType == 'NAME': WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.NAME, reqText)))
    except Exception:
        waitResault='[error] Элемент, не найден "' + reqText + '"'
        print(waitResault)
        exit(10)
    else:
        waitResault = '[Элемент Найден] "' + reqText + '"'
        print(waitResault)






