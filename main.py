import proses
import xlrd 
import openpyxl
from xlrd import open_workbook


wb=open_workbook('/home/halim/Documents/Sent_Analisis/Data_Labeled.xlsx')
dataTrain=wb.sheet_by_index(0)
rowLen=dataTrain.nrows

	#file output
fp=openpyxl.Workbook()
dp=fp.active
for i in range(rowLen): 
	data_i=dataTrain.cell(i,0).value
	prep=proses.preprocess(data_i)
	print prep
	"""
	if prep: 
		for i in range(len(prep)):
			dp.append([''.join(prep[i])])
fp.save('hasil.xlsx')
			
"""
