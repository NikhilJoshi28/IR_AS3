import numpy
import pandas as pd
import xlwt
import xlrd
import math
import csv

path = '/home/tex/Documents/IR/Dataset_AS3/'
filename = 'finaldata.xls'
#data = pd.ExcelFile(path+filename)

xlsfile = xlrd.open_workbook(path+filename, on_demand= True)
xlsfiledata = xlsfile.sheet_by_index(0)

#print(xlsfiledata.cell(0,0).value)

rowavg =[]
for i in range(0,25536):
    sum=0
    #print(i)
    for j in range(1,101):
        value = xlsfiledata.cell(i,j).value
        if value>=-10 and value<=10:
            sum=sum+value
    rowavg.append(sum/xlsfiledata.cell(i,0).value)

similarity = []
for i in range(0,20):
    similarity.append([])
    print(i)
    similarity[i].append(1)
    for j in range(i+1,20):
        sum1=0
        sum2=0
        sum3=0
        for k in range(1,101):
            val1 = xlsfiledata.cell(i,k).value
            val2 = xlsfiledata.cell(j,k).value
            if val1!=99 and val2!=99:
                sum1=sum1+((val1-rowavg[i])*(val2-rowavg[j]))
                sum2=sum2+((val1-rowavg[i])*(val1-rowavg[i]))
                sum3=sum3+((val1-rowavg[j])*(val1-rowavg[j]))

        sim= sum1/((math.sqrt(sum2))*(math.sqrt(sum3)))
        similarity[i].append(sim)

print(len(similarity[18]))
my_df = pd.DataFrame(similarity)
my_df.to_csv(path+'similarity20.csv',index=False,header=False)
