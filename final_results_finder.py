import os
import pandas as pd
directory = input("enter the tar file name \n")
cmd = "unar "+directory
os.system(cmd)
directory = directory.replace(".tar.gz","")
directory = directory.replace(" ","")
lst = os.scandir(directory)
files = []
dirs = []
def find_files(lst,files):
    for entry in lst :
        if entry.is_file():
            #print(entry.name)
            files.append(str(entry.name))
    return files
def unarchive_files(files,directory):
    for i in files:
        cmd = "unar "+directory +"/"+str(i)+ " -o " +directory
        os.system(cmd)

def find_dirs(lst,dirs):
    dirs.clear()
    lst = os.scandir(directory)
    for entry in lst :
        if entry.is_dir():
            dirs.append(str(entry.name))
    return dirs
def rename_dirs(dirs,directory):
    os.chdir(directory)
    for i in range(len(dirs)):
        new = 'Round_'+ str(i+1)
        os.rename(dirs[i],new)
    os.chdir("..")
def copy_matrix_file(dir_lst,directory):
    os.chdir(directory)
    os.mkdir("Final_matrix")
    for i in dir_lst:
        old = str(i)+"/Matrix.csv"
        new = str(i)+"/"+str(i)+"_matrix.csv"
        os.rename(old,new)
        cmd = "cp "+ new +" Final_matrix"
        os.system(cmd)
print(find_files(lst,files))
unarchive_files(files,directory)
print(find_dirs(lst,dirs))
rename_dirs(dirs,directory)
print(find_dirs(lst,dirs))
copy_matrix_file(find_dirs(lst,dirs),directory)
print(os.getcwd())
# reset for codes completed
files =  []
x = directory
dirc = 'Final_matrix/'
lst1 = lambda dirc : os.scandir(dirc)
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
def find_files(lst1,files):
    for i in lst1:
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
print(find_files(lst1(dirc),files))
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
print(os.getcwd())
#Final Matrix generated
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
    wrtie_to_file("Matrix2.csv",'wb',res)
    wrtie_to_file("Matrix3.csv",'wb',res)
    lis = df.values.tolist()
    return lis
def change_to_float(x):
    for i in range(0,len(x)):
        for j in range(1,4):
          #  x[i][j] = x[i][j].replace("'","")
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
x = get_matrix("Matrix.csv")
change_to_float(x)
Mat2 = ['Data Processing Strength', "Computational Strength"]
Mat2_intervels = [0,4,len(x)]
for i in range(len(Mat2)):
    lst2 = [Mat2[i]]
    lst2.extend(find_avg(x,Mat2_intervels[i],Mat2_intervels[i+1]))
    wrtie_to_file("Matrix2.csv",'ab',lst2)
Mat3 = ['Data Transferring Strength', "Data Encoding/ Decoding Strength", "Instruction Handling Strength", "Arithmetic Calculation Strength","Float Calculation Strength"]
Mat3_intervels = [0,2,4,7,10,len(x)]
for i in range(len(Mat3)):
    lst2 = [Mat3[i]]
    lst2.extend(find_avg(x,Mat3_intervels[i],Mat3_intervels[i+1]))
    wrtie_to_file("Matrix3.csv",'ab',lst2)