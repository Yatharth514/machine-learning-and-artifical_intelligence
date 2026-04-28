import os   
from datetime import datetime
print(os.getcwd())
os.chdir('/Users/Lenovo/ai_ml/')
print(os.listdir())

os.chdir("/Users/Lenovo/")
# # os.mkdir("Level-1")#it will not create the sub-folders with it 
# os.makedirs("Level-2/Sub-Level")
# os.removedirs("Level-2/Sub-Level") from this we can remove the file 

# os.rename("Level-1","Level-0") we can rename this 

# mod_time =(os.stat("Level-0").st_mtime)

# print(datetime.fromtimestamp(mod_time))


# print(os.listdir())

# for dirpath, dirnames ,filenames in os.walk("/Users/Lenovo/"):
#     print("Current Path :",dirpath)
#     print("Directories : ",dirnames)
#     print("Files : ",filenames)
#     print()

print(os.environ.get("Lenovo" ))

