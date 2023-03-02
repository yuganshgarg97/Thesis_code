import os
import pandas as pd
files =  []
def filter_data(res):
    y = str(res)
    y = y.replace("[","")
    y = y.replace("]","")
    y = y.replace("\n","")
    y = y + "\n"
    y = y.encode()
    return y
def wrtie_to_file(file_name,mode, res):
    f = open(file_name,mode)
    y = filter_data(res)
    f.write(y)
    f.close()
def get_matrix(file_name):
    df = pd.read_csv (file_name)
    res = df.columns.tolist()
    wrtie_to_file("../results/Matrix2.csv",'wb',res)
    wrtie_to_file("../results/Matrix3.csv",'wb',res)
    lis = df.values.tolist()
    return lis
def change_to_float(x):
    for i in range(0,len(x)):
        for j in range(1,4):
            x[i][j] = x[i][j].replace("'","")
            x[i][j] = float(x[i][j])
def find_avg(Mat,start,end):
    Mem_avg = 0.0
    Cpu_avg = 0.0
    Total_time = 0.0
    tmp1,tmp2 = 0.0,0.0
    for i in range(start,end):
        Total_time += Mat[i][1]
        tmp1 += Mat[i][1]*Mat[i][2]
        tmp2 += Mat[i][1]*Mat[i][3]
    Cpu_avg = tmp1/Total_time
    Mem_avg = tmp2/Total_time
    return [Total_time,Cpu_avg,Mem_avg]
x = get_matrix("../results/Matrix.csv")
change_to_float(x)
Mat2 = ['Data Processing Strength', "Computational Strength"]
Mat2_intervels = [0,4,len(x)]
for i in range(len(Mat2)):
    lst = [Mat2[i]]
    lst.extend(find_avg(x,Mat2_intervels[i],Mat2_intervels[i+1]))
    wrtie_to_file("../results/Matrix2.csv",'ab',lst)
Mat3 = ['Data Transferring Strength', "Data Encoding/ Decoding Strength", "Instruction Handling Strength", "Arithmetic Calculation Strength","Float Calculation Strength"]
Mat3_intervels = [0,2,4,7,10,len(x)]
for i in range(len(Mat3)):
    lst = [Mat3[i]]
    lst.extend(find_avg(x,Mat3_intervels[i],Mat3_intervels[i+1]))
    wrtie_to_file("../results/Matrix3.csv",'ab',lst)



