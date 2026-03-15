# A Program to search a file location anywhere in the system / device. The  filename be entered by the user
import os 

# in case the file is loacted anywhere
def serach_file_location(fn:str)->str:
    current_directory=os.getcwd()
    parent_dir =os.path.abspath(os.path.join(current_directory,os.pardir))
    loc =[]; flag=False
    dir_path = os.path.dirname(parent_dir)
    
    for root,dirs,files in os.walk(dir_path):
        for file in files:
            if file==fn:
                loc.append(root+os.sep+str(file))
                flag=True
    return flag,loc

# in case the file is located in the same folder
def serach_file_location_infolder(fn:str)->str:
    current_directory=os.getcwd()
    loc =[]; flag=False
    
    for root,dirs,files in os.walk(current_directory):
        for file in files:
            if file==fn:
                loc.append(os.path.join(root,file))  # use  os.path.join for proper path construction
                flag=True
        if flag:
            break
        
    return flag,loc   
    