import Util
import Web

filename = Util.WorkExcel().FileNameStartParam()


def OperaionMainDef(filename,nameWorksheets):
    # Получить список операций
    stepList = Util.WorkExcel().readStepList(filename,nameWorksheets)

    for operation in stepList:
        print('nnnn' + operation[1])
        if operation[1]=='Сценарий':
            print('Запущен внешний сценарий')
            for itemParam in operation:
                spParam = itemParam.split('=')
                nameParam = spParam[0]
                if nameParam == 'Документ': documName = spParam[1]
                if nameParam == 'Имя листа': nameWorksheets = spParam[1]
            if documName == 'Текущий':
                print(filename+ ' -' +nameWorksheets)
                OperaionMainDef(filename, nameWorksheets)
        else:
            answerOperation = Web.Operation().toExecute(operation)
        print(answerOperation)


OperaionMainDef(filename,'Сценарий')





