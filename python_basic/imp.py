import my_module
import sys

course=["Maths","Physics","Chemistry","Biology"]

index=my_module.find_index(course,"Maths")
print(f"The index of the Maths is {index}")

# we could also do this :
from my_module import find_index

course=["Maths","Physics","Chemistry","Biology"]

print(f"The index of the Maths is : {find_index(course,'Maths')}")

print(sys.path)

