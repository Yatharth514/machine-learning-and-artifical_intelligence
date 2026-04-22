algorithm_name="Kandane"
dataset_size=56
accuracy_score=96.59
is_deployed=False

dataset_name=input("Enter the name of the dataset :")
print(f"Initializing pipeline for the {dataset_name} dataset...")
user_input=int(input("Enter the weight of the neural network :"))
convert=float(user_input)*0.5

epochs=int(input("Enter the total number of the epochs:"))
seconds_per_epoch=float(input("Enter the seconds per epoch : "))
time_taken = float(epochs)*seconds_per_epoch
print(f"The total time taken in training is :{time_taken}")

true_positives=85
false_positives=15
Precision=float((true_positives)/(true_positives+false_positives))*100.00
print(f"The precision of the machine is : {Precision}%")

user2_input=int(input("Enter the image pixel value which ranges from 0 to 255 : "))
normalized_value=float(user2_input/255)
print(f"The noramlized value {normalized_value:.3f}")