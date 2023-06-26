import openpyxl
import os, sys
import lxml.etree
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import argparse

class UfosAutotestUtil:

    def SessionOpen(self):
        self.driver = webdriver.Firefox()
        print('Версия браузера: ' + '{}: {}'.format(
            self.driver.capabilities['browserName'],self.driver.capabilities['browserVersion']))
        return self.driver


    def opSessionClose(self, driver):
        self.driver = webdriver.close()


    def waitElement(self, driver,reqText, reqType='XPATH',timer=60 ,typeSearch = 'presence_of_element_located'):
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
                else: print("                (Ожидание обработки страницы )", i, "сек")
            if i==60:
                print("[error] Превышено время ожидания")
                exit(10)

#Проверяем наличие элемента
        try:
            if typeSearch == 'presence_of_element_located':
                if reqType == 'XPATH': WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.XPATH, reqText)))
                if reqType == 'ID': WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.ID, reqText)))
                if reqType == 'NAME': WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.NAME, reqText)))
                if reqType == 'CSS': WebDriverWait(driver, timer).until(EC.presence_of_element_located((By.CSS_SELECTOR, reqText)))

        except Exception:
            waitResault='[error] Элемент, не найден "' + reqText + '"'
            print(waitResault)
            exit(10)
        else:
            waitResault = '                (Элемент Найден) "' + reqText + '"'
            print(waitResault)


# Выводит сообщения в консоль
    def printConsoleStep(self, stepNote):
        txt = '[Выполняется] ' + stepNote['Step'] + ' ' + stepNote['Name'] + ' ('
        for key in stepNote:
            if not(key == 'Step' or key == 'Name'):
                txt= txt + key + ':' + stepNote[key] + ' '
        print(txt + ')')
    y=1






# Дополнить stepListIn системными именами функций из listOperation
    def updateStepListSystemName(self, stepListIn,listOperation):
        #Проходим по всем шагам сценария
        step=0
        for itemStep in stepListIn:

            name = stepListIn[itemStep]['Name'].split('.')
            if len(name)==2:
                if (listOperation[name[0]]['systemName'] and listOperation[name[0]][name[1]]['systemName']):
                    sysName = listOperation[name[0]]['systemName'] + '.' + listOperation[name[0]][name[1]]['systemName']
                    stepListIn[itemStep]['sysName']= sysName
                else:
                    print('[error] Не найдено описание команды: ' + stepListIn[itemStep]['Name'])
        return stepListIn

    def readExcelFile(self, fileName, nameWorksheets='Сценарий',stepList={},step=1):
        print(fileName + ' ' + nameWorksheets)
        if os.path.exists(fileName):
            print("Файл " + fileName + " найден")
        else:
            print("Файл " + fileName + " не найден")
            exit(2)
        wb = openpyxl.load_workbook(filename=fileName)
        ws = wb.get_sheet_by_name(nameWorksheets)
        rows = ws.iter_rows()
        data_gen = [[cell.value for cell in row] for row in rows]

        for rowsNumber in data_gen:
            if rowsNumber[0]:
                if rowsNumber[1]=='Дополнительный сценарий':

                    spParamDoc=rowsNumber[2].split('=')
                    spParamList = rowsNumber[3].split('=')
                    if spParamDoc[0]=='Документ' and spParamDoc[1]=='Текущий':
                        fileName=fileName
                    else:
                        fileName=spParamDoc[1]
                    nameWorksheets=spParamList[1]

                    stepList, step = readExcelFile(fileName=fileName, nameWorksheets = nameWorksheets,stepList=stepList, step=step)
                    x=1
                else:

                    oper={}
                    if len(rowsNumber)>=2:
                        for itemOper in rowsNumber[2:]:
                            oper['Step'] = rowsNumber[0]
                            oper['Name'] = rowsNumber[1]
                            if itemOper:
                                spParam = itemOper.split('=')
                                oper[spParam[0]]= spParam[1]
                    stepList[step] = oper
                step = step + 1
        return stepList,step




# Чтение настроек списка команд
    def ReadListOperation(self):
        pramInit = lxml.etree.parse("OperationNote.xml")
        XmlOperationGroup = pramInit.getroot().xpath(".//operationType")
        operationGroup={}
        for item1 in XmlOperationGroup:
            name = item1.attrib['Name']
            operationGroup[name] = item1.attrib
            Xmloperation=item1.xpath(".//operation")
            operationName = {}

            for item2 in Xmloperation:
                name2 = item2.attrib['Name']
                operationName[name2]=item2.attrib
                XmlVariable=item2.xpath(".//variable")
                variableName = {}

                for item3 in XmlVariable:
                    name3 = item3.attrib['Name']
                    variableName[name3] = item3.attrib

                operationName[name2] = dict(operationName[name2], **variableName)
            operationGroup[name] = dict(operationGroup[name],**operationName)
        return operationGroup







# Чтение файла с настройками setup.ini
# Настройки из setup.ini передаются в iniServSelenium,iniStend,initUsers
    def readStartInitParam(self):

        pramInit = lxml.etree.parse("setup.ini")
        pramServSelenium = pramInit.getroot().xpath(".//Selenium/Server")

        iniServSelenium = {}
        for item in pramServSelenium:
            name = item.attrib['name']
            iniServSelenium[name]=item.attrib

        pramStends = pramInit.getroot().xpath(".//Stends/Stend")
        iniStend  = {}
        initUsers = {}
        for item in pramStends:
            name = item.attrib['name']
            iniStend[name] = item.attrib

            itemsD={}
            for items in item.xpath(".//Users/User"):
                nameItems = items.attrib['name']
                itemsD[nameItems]=items.attrib

            initUsers[name] = itemsD
        return iniServSelenium,iniStend,initUsers

    def readParams(self):
        arg_parser = argparse.ArgumentParser(description='')
        arg_parser.add_argument('-u', '--user-name', action='store',
                                help='Имя пользователя')
        arg_parser.add_argument('-ul', '--user-password', action='store',
                                help='Пароль пользователя')

        args = arg_parser.parse_args()
        if args.user_name:
            user_name = args.user_name
        else:
            sys.exit()

        if args.user_password:
            user_password = args.user_password
        else:
            sys.exit()
        return user_name, user_password
# Примеры получения значений из переменных
#    x1 = iniServSelenium['S1']['Browser']
#    x2 = iniStend['DEV']['Url']
#    x3 = initUsers['DEV']['RO']['login']