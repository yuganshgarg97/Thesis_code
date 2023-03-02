import os
import pandas as pd
files =  []
x = input("Enter directory name \n")
dirc = str(x) + '/Final_matrix'
lst = lambda dirc : os.scandir(dirc)
def get_matrix(file_name):
    df = pd.read_csv (file_name)
    res = df.columns.tolist()
    f = open("Matrix.csv",'wb')
    y = str(res)
    y = y.replace("[","")
    y = y.replace("]","")
    y = y.replace("\n","")
    y = y + "\n"
    y = y.encode()
    f.write(y)
    f.close()
    print (df)
    print(type(df))
    lis = df.values.tolist()
    return lis
def find_files(lst,files):
    for i in lst:
        if i.is_file():
            files.append(i.name)
    return files
def to_flt(s):
    s = s.replace("'","")
    s = float(s)
    return s
def find_avg(x):
    r =[]
    for i in range(len(x[0])):
        r1 = []
        r1.append(x[0][i][0])
        for j in range(1,4):
            r1.append(x[0][i][j] + x[1][i][j] + x[2][i][j] +x[3][i][j] + x[4][i][j])
        r.append(r1)
    #print(r)
    for i in range(len(r)):
        for j in range(1,4):
            r[i][j] = r[i][j]/5
    #print(r)
    return r
def write_to_file(res):
    f = open("Matrix.csv",'ab')
    y = str(res)
    y = y.replace("[","")
    y = y.replace("]","")
    y = y.replace("\n","")
    y = y + "\n"
    y = y.encode()
    f.write(y)
    f.close()
print(find_files(lst(dirc),files))
os.chdir(dirc)
x = []
for i in files:
    x.append(get_matrix(i))
for i in range(len(x)):
    for j in range(len(x[i])):
        for k in range(1,4):
           x[i][j][k] = to_flt(x[i][j][k])
result = find_avg(x)
for i in range(len(result)):
    write_to_file(result[i])
