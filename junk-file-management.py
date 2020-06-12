"""
AUTHOR -Arvind kumar 

"""


import os
import shutil
import os.path, time
from datetime import datetime
from pathlib import Path
import math
# package 
# This function organize file by extension 

def sortByExtension():
    dir_path = input("Enter Your directory :--")
    lis = os.listdir(dir_path)
    lis.sort(key=lambda x: os.stat(os.path.join(dir_path, x)).st_mtime)
    # find files in folder 
    files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f))]
    print(files)   #you can see files name in terminal 

    # change dir refer -https://www.tutorialspoint.com/python/os_chdir.htm
    os.chdir(dir_path)
    arr = os.listdir()
    print(arr) 
    slash = '\\'

    # all file types 

    file_types = {
        "Text" : [ ".doc",".rtf",".txt", ".wps",".docx" ],
        "Data" : [ ".csv" , ".pps" , ".ppt" , ".pptx" ,".xml" ],
        "Audio" : [".m4a" , ".mp3" ],
        "Video" : [ ".3g2" , ".3gp" , ".avi" , ".flv" , ".m4v" , ".mov" , ".mp4" , ".mpg", ".wmv" ],
        "notes" : [ ".pdf" ],
        "Spreadsheet" : [ ".xlr" , ".xls" , ".xlsx" ],
        "apps" : [ ".apk" , ".app", ".exe"  , ".jar"  ],
        "Web" : [ ".css" , ".htm" , ".html" , ".js" , ".php" , ".xhtml" ],
        "Compressed" : [ ".rar", ".zip" ],
        "Developer" : [ ".c" , ".class" , ".cpp" , ".cs" , ".java" , ".py" ],
        "Misc" : [ ".ics" , ".msi"  , ".torrent" ]
    }

    for x in arr:
        flag = False #bool
        if os.path.isfile(x):
            if("." in x):
                extension_name = x[x.index("."):]
                for file_type,extensions in file_types.items():
                    # cross check if file_type,extension in our dir then find it 
                    if extension_name in extensions:
                        flag = True
                        folder = file_type
                        newpath = dir_path+slash+folder
                        print(newpath)
                        break
                    # Here suppose x.jsx , then this extension is not there then , its store in Other folder 
                    if (flag==False):
                        folder_name ="Other"
                        newpath = dir_path + slash + folder_name
            # Here is create dir
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.move(dir_path + slash + x,newpath + slash +x)

# Sort by date 

def SortByDate():
    path = input("enter path directory :-")
    lis = os.listdir(path)
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_mtime)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    os.chdir(path)


    for x in files:
        # creation_time,modified_time,cretion_Date,modified_date
            creation_time_string = time.ctime(os.path.getmtime(os.path.join(path, x)))
            modified_time_string = time.ctime(os.path.getmtime(os.path.join(path, x)))
            creation_datetime_obj = datetime.strptime(creation_time_string, '%a %b %d %H:%M:%S %Y')
            modified_datetime_obj = datetime.strptime(modified_time_string, '%a %b %d %H:%M:%S %Y')
            modified_date  = str(modified_datetime_obj.day) + '-' +str(modified_datetime_obj.month) + '-'+str(modified_datetime_obj.year)
            
            if (os.path.isdir(modified_date)):
                shutil.move(os.path.join(path,x),modified_date)
            else:
                os.makedirs(modified_date)
                shutil.move(os.path.join(path,x),modified_date)


units = {"B": 1, "KB": 10**3, "MB": 10**6, "GB": 10**9, "TB": 10**12}

def SortBySize():


    path = input("enter path directory :-")
    # size= Path(path).stat().st_size
    lis = os.listdir(path)
    
    lis.sort(key=lambda x: os.stat(os.path.join(path, x)).st_size)
    
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    os.chdir(path)

    for x in files:
        size= Path(x).stat().st_size
        if size == 0:
            return "0B"
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size, 1024)))
        p = math.pow(1024, i)
        s = round(size / p, 2)
        sizefile="%s %s" % (s, size_name[i])
        if sizefile >= '6 KB':
            print(sizefile)
            os.makedirs('Big file')
            shutil.move(os.path.join(path,x),'Big file')
        elif sizefile<='6 KB':
            os.makedirs('Small file')
            shutil.move(os.path.join(path,x),'Small file')
def close():
    return

print("""PRESS 1 TO ORGANIZE FILES BY EXTENSION
PRESS 2 TO  ORGANIZE FILES BY DATE
PRESS 3 TO  ORGANIZE FILES BY SIZE
PRESS 4 TO EXIT OUR APPLICATION""")
            
        
       
        


   

    



option=int(input("ENTER YOUR OPTION:-"))
if option==1:
    sortByExtension()
elif option == 2:
    SortByDate()
elif option == 3:
    SortBySize()
elif option == 4:
    close()


    
