import os
class Files :
    def __init__(self,filepath,filemoode) :
        self.Filepath=filepath
        self.Filemoode=filemoode
        self.Object=None

    def __enter__(self) :
        self.Object=open(self.Filepath,self.Filemoode)
        return self.Object
    
    def __exit__(self,*exc) :
        if self.Object :
            self.Object.close()

try :
    def createfileedit(linelist,moode) :
        os.mkdir("NewFolder")
        os.chdir("NewFolder")
        with Files("files_in_python_edit.txt",moode) as file1 :
            for line in linelist :
                file1.write(line)
        size=os.path.getsize("C:/Users/digi kala/Desktop/Python/NewFolder/files_in_python_edit.txt")
        basename=os.path.basename("C:/Users/digi kala/Desktop/Python/NewFolder/files_in_python_edit.txt\n")
        with Files("description.txt","a") as file2 :
            file2.write(basename)
            file2.write(str(size/1024))
except Exception as eror :
    print(eror)

try :
    with Files("files_in_python.txt","r") as file1 :
        linelist=[]
        for line in file1.readlines() :
            if "inbuilt" in line :
                linelist.append(line.replace("inbuilt","built-in"))
            else :linelist.append(line)
        createfileedit(linelist,"a")    
             
except Exception as eror :
    print(eror)