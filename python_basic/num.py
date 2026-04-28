import numpy as np 
arr=[1,2,3,4,5,6]
num_arr=np.array(arr)

ten_times=num_arr*10
print(f"Ten times : {ten_times}")

actual_prices=np.array([10,20,30])
predicted_prices=np.array([12,18,33])
print(f"Error :{predicted_prices-actual_prices}")

data=np.array([45,88,92,16,67])
print(f"The max : {data.max()}")
print(f"The mean : {data.mean()}")

arra=np.zeros(10)
arra[4]=1
print(arra)

marks=np.array([[80,90],[70,75],[95,99]])
print(marks)
print(f"The shape is : {marks.shape}")

raw_data=np.array([10,20,30,40,50])
mean_of_raw_data=raw_data.mean()
print(f"The mean : {mean_of_raw_data}")
new_array=raw_data-mean_of_raw_data
print(new_array)