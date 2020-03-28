import xlrd
import xlsxwriter
import uuid

uniqueKeys = {
}


file_location = r'file-location'
wb = xlrd.open_workbook(file_location)
sh = wb.sheet_by_index(0)

for key in uniqueKeys:
    inputKey = key
    randomNumber = uuid.uuid4()
    fileName = ''+str(randomNumber)+'-'+str(inputKey)+'.xlsx'
    workbook = xlsxwriter.Workbook('file-location'+fileName)
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, 'Header 0')
    worksheet.write(0, 1, 'Header 1')
    worksheet.write(0, 2, 'Header 2')
    worksheet.write(0, 3, 'Header 2')
    workSheetRow = 1
    for col in sh.get_rows():
        col0 = int(col[0].value)
        col1 = str(col[1].value).strip(".0")
        col2 = str(col[2].value)
        col3 = float(col[3].value)
        if sellerIds == inputSeller:
            worksheet.write(workSheetRow, 0, col0)
            worksheet.write(workSheetRow, 1, col1)
            worksheet.write(workSheetRow, 2, col2)
            worksheet.write(workSheetRow, 3, col3)
            workSheetRow = workSheetRow + 1
    workbook.close()