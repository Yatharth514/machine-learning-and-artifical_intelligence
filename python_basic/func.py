def recur(n):
    if(n==1 or n==0):
        return n
    else:
        return n*recur(n-1)
    
n =int(input("Enter the number : "))
print(recur(n))

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

print(student_info("Maths","Arts",name="Yatharth",age=22))

def stu_info(*args,**kwargs):
    print(args)
    print(kwargs)

course=["Maths","Physics"]
info={"name":"Yatharth","age":19}
stu_info(*course,**info)