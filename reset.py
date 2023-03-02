import os
directory = input("enter the tar file name \n")
cmd = "unar "+directory
os.system(cmd)
directory = directory.replace(".tar.gz","")
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
