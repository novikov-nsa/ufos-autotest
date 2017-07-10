import openpyxl


class WorkExcel(object):
    def readStepList(self,fileName):
        wb = openpyxl.load_workbook(filename=fileName)
        ws = wb.worksheets[0]
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



