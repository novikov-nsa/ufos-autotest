import Util
import OperationNavigation
import OperationScroll
import OperationVisualForm



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


# Запуск сценария
driver = Util.SessionOpen()
for stepItem in stepListIn:
    Util.printConsoleStep(stepListIn[stepItem])
    command = stepListIn[stepItem]['sysName']+'(driver,stepListIn[stepItem])'
    eval(command)






y=1


