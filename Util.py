import openpyxl
import os,sys



class WorkExcel(object):
#Проверка правильности пути к файлу шаблона, заданного в параметрах запуска
    def FileNameStartParam(self):
        if len(sys.argv) > 1:
            filename = sys.argv[1]
            #filename = sys.path[0] + sys.argv[1] #Если нужен относительный путь
            if os.path.exists(filename):
                print("Файл " + filename + " найден")
            else:
                print("Файл " + filename + " не найден")
                exit(12)
        else:
            print("Имя файла шаблона не указано")
            exit(13)
        return filename

    #Получить из Excel писок операци
    def readStepList(self,fileName,nameWorksheets):

        print(fileName+' ' +nameWorksheets)
        wb = openpyxl.load_workbook(filename=fileName)
        ws = wb.get_sheet_by_name(nameWorksheets)
        rows = ws.iter_rows()
        data_gen = [[cell.value for cell in row] for row in rows]

        stepList = list()
        rowsNumbers = list()

        for rowsNumber in data_gen:
            if rowsNumber[0]:
                rowsNumbers = list()
                for items in rowsNumber:
                    if items:
                        rowsNumbers.append(items)
                stepList.append(rowsNumbers)

        return stepList
    pass



