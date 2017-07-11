import UtilExcelRead
import Web
import sys
import os


#Проверка на наличие файла со списком операций. Файл передается как параметр.
#Пример: python AuotoTest.py ./Шаблоны/D01_S_000_000.xlsm
if __name__ == "__main__":
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if os.path.exists(filename):
            print("Файл "+filename+" найден")
        else:
            print("Файл " + filename + " не найден")
            exit(12)
    else:
        print("Имя файла шаблона не указано")
        exit(13)

#Получить список операций
stepList = UtilExcelRead.WorkExcel().readStepList(filename)

#Выполнение операций
for operation in stepList:
    answerOperation = Web.Operation().toExecute(operation)
    print(answerOperation)