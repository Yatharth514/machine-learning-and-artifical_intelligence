import os 
os.chdir("/Users/Lenovo/ai_ml/python_basic/")
print(os.getcwd())
with open("test.txt","r") as f:
    # f_contents=f.read(100 )
    # print(f_contents)

    # for line in f:
    #     print(line,end=" ")

    size_to_read=10

    f_contents=f.read(size_to_read)
    print(f_contents,end=" ")
    f.seek(0)
  
    f_contents=f.read(size_to_read)
    print(f_contents,end=" ")
    # print(f.tell())

    # while len(f_contents)>0:
    #     print(f_contents,end=" ")
    #     f_contents=f.read(size_to_read)




    


# f=open("test.txt","r")#this is to open the file 
 
# print(f.name)
# print(f.mode) 
# f.close()

with open("Test2.txt","w") as f:
    f.write("Test")