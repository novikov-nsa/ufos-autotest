from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import OperationBase

class OperationIterator(object):
    def toExecute(self,setOperation):
        nameOperation = setOperation[0]
        typeOperation = setOperation[1]
        print(nameOperation,typeOperation)
        resaultOperation = 'Начало выполнения'

        if typeOperation == 'Итератор.Нажать кнопку в строке':              resaultOperation = Operation().opLogin(setOperation)

        def opButton(self, setOperation):
            # Операция "Кнопка"
            # Возможные параметры
            # Название

            # Выставить параметры
            elemPos = '1'
            for itemParam in setOperation:
                spParam = itemParam.split('=')
                nameParam = spParam[0]
                if nameParam == 'Название': keyName = spParam[1]
                if nameParam == 'Порядок': elemPos = spParam[1]

            xpathSt = "//button[text()='" + keyName + "'][" + elemPos + "]"
            OperationBase.waitElement(xpathSt)
            # driver.find_element_by_xpath(xpathSt).click()

            element = OperationBase.driver.find_element_by_xpath(xpathSt)
            ActionChains(OperationBase.driver).move_to_element(element).click(element).perform()

            resaultOperation = '[Операция выполнена -] ' + setOperation[1]
            return resaultOperation

        return resaultOperation