import Util
import OperationBase

filename = Util.WorkExcel().FileNameStartParam()


def OperaionMainDef(filename,nameWorksheets):
    # Получить список операций
    stepList = Util.WorkExcel().readStepList(filename,nameWorksheets)

    for operation in stepList:
    #Запуск внешнего сценария
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
                print(documName + ' -' + nameWorksheets)
                OperaionMainDef(documName, nameWorksheets)
        else:
            spOperation = operation[1].split('.')
            #Запуск основных операци
            if len(spOperation) == 1:
                answerOperation = OperationBase.Operation().toExecute(operation)

            # Запуск дополнительных операций
            if len(spOperation) > 1:
                answerOperation = OperationBase.Operation().toExecute(operation)
            print(answerOperation)


OperaionMainDef(filename,'Сценарий')
OperationBase.opSessionClose()
print('Тест завершен')





