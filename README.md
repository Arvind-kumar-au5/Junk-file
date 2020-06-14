#Junk File Mangemnet 
 Basically, as a lazy programmer my desktop is full of files (Junk Files), Junk file managemnet is a program for dealing with junk file


## Installation 
```
Python 3.4
```
## Usage
```
run command 
python junk-file-management.py
Output
PRESS 1 TO ORGANIZE FILES BY EXTENSION
PRESS 2 TO  ORGANIZE FILES BY DATE
PRESS 3 TO  ORGANIZE FILES BY SIZE
PRESS 4 TO EXIT OUR APPLICATION
```

## Learn 
```
# I learn -
>1. How to deal with os package 
exmample-
import os.path, time
dir_path = input("Enter Your directory :--")
lis = os.listdir(dir_path)


>Here you can see how to find dir

>2. How to change byte to KB 
>example
units = {"B": 1, "KB": 10**3, "MB": 10**6, "GB": 10**9, "TB": 10**12}
size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
i = int(math.floor(math.log(size, 1024)))
p = math.pow(1024, i)
s = round(size / p, 2)
sizefile="%s %s" % (s, size_name[i])
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
