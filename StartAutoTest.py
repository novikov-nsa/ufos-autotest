import Util
import OperationNavigation
import OperationScroll
import OperationVisualForm
import OperationIterator



# Чтение начальных настроек из setup.ini
iniServSelenium, iniStend, initUsers = Util.readStartInitParam()
# Чтение параметров из строки запуска
iniArg = Util.readStartParam()
# Чтение сценария
stepListIn = Util.readExcelFile(iniArg['FileName'])[0]
# Чтение списка операций из OperationNote.xml
listOperation = Util.ReadListOperation()
# Дополнить stepListIn системными именами функций из listOperation
stepListIn = Util.updateStepListSystemName(stepListIn, listOperation)

variablesParam = {}
resaultStep = {}


# Запуск сценария
driver = Util.SessionOpen()
for stepItem in stepListIn:

    #Подставляем переменные
    for varItem in stepListIn[stepItem]:
        valueParam = stepListIn[stepItem][varItem]
        #Поиск переменной которую нужно подставить (формат ${Имя переменной})
        if valueParam[:2]=='${':
            varTextIn = valueParam[2:(len(valueParam)-1)]
            if varTextIn in variablesParam:
                x = variablesParam[varTextIn]
                #Подставляем значение переменной
                stepListIn[stepItem][varItem]=variablesParam[varTextIn]

    Util.printConsoleStep(stepListIn[stepItem])
    #Запуск операции
    command = stepListIn[stepItem]['sysName']+'(driver,stepListIn[stepItem])'
    resaultStep  = eval(command)

    #Обработка результата операции
    stepListIn[stepItem]['Статус'] = resaultStep['Статус']
    if 'Переменная' in resaultStep:
        variablesParam[resaultStep['Переменная']['Имя параметра']] = resaultStep['Переменная']['Значение']









