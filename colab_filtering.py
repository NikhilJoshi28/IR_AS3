import pandas as pd
import xlrd
import math
import csv

path = '/home/tex/Documents/IR/Dataset_AS3/'
filename = 'similarity5000.csv'
with open(path+filename, 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

sim = []
for i in range(len(your_list)):
    sim.append([])
    for j in range(len(your_list[i])):
        if your_list[i][j]=='':
            pass
        else:
            sim[i].append(float(your_list[i][j]))

filename2 = '5000dataset.xls'

xlsfile = xlrd.open_workbook(path+filename2, on_demand= True)
xlsfiledata = xlsfile.sheet_by_index(0)

data=[]
for i in range(0,5000):
    data.append([])
    for j in range(1,101):
        data[i].append(xlsfiledata.cell(i,j).value)

#print(data[0])

colab_fil = []
for i in range(0,5000):
    colab_fil.append([])
    print(i)
    for j in range(0,100):
        if data[i][j]==99:
            sum1=0
            sum2=0
            for k in range(0,5000):
                if k==i:
                    pass
                else:
                    if i<k and sim[i][k-i]>0 and data[k][j]!=99:
                        sum1 = sum1 + (float(data[k][j])*float(sim[i][k-i]))
                        sum2 = sum2 + float(sim[i][k-i])
                    elif i>k and sim[i-k][k]>0 and data[k][j]!=99:
                        sum1 = sum1 + (float(data[k][j])*float(sim[i-k][k]))
                        sum2 = sum2 + float(sim[i-k][k])

            value = sum1/sum2
            colab_fil[i].append(value)
            #data[i][j]=value
        else:
            colab_fil[i].append(data[i][j])

my_df = pd.DataFrame(colab_fil)
my_df.to_csv(path+'colab5000.csv',index=False,header=False)