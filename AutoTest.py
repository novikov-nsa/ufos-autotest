import UtilExcelRead
import Web
import sys
import os

#Получить список операций

if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.path.exists(filename):
            print("Файл "+filename+" найден")
        else:
            print("Файл " + filename + " не найден")
            exit(12)
    else:
        filename = './Шаблоны/D01_S_000_000.xlsm'

#        print("Имя файла шаблона не указано")
#        exit(13)

#'./Шаблоны/D01_S_000_000.xlsm'
stepList = UtilExcelRead.WorkExcel().readStepList(filename)

#Выполнение операции
for operation in stepList:
    answerOperation = Web.Operation().toExecute(operation)
    print(answerOperation)