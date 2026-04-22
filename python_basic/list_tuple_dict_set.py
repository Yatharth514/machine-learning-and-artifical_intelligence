accuracy=[95.1,25.3,47,36.4,78.2]
print(accuracy)
accuracy.append(16.2)
accuracy.sort()
print(accuracy)

model_metrics=("GPT","55.23","26")
model,acc,time_taken=model_metrics
print(f"The model {model} with accuracy {acc} takes {time_taken} minutes.")

class_counts={
    "cats":150,
    "dogs":200
}
class_counts["birds"]=50
class_counts["cats"]+=25
print(class_counts)

vocab={
    "AI":0,
    "Python":1,
    "Data":2
}
user_input=input("Enter the data to be accessed : ")
print(f"The word which you accessed is :{vocab[user_input]}")

text_data = ["the", "robot", "saw", "the", "dog", "and", "the", "robot", "learned"]
unique_data=set(text_data)
print(len(unique_data))

batch = [
    # First dictionary (Index 0)
    {
        "id": 101, 
        "features": [0.88, 0.12]
    },
    
    # Second dictionary (Index 1)
    {
        "id": 102, 
        "features": [0.45, 0.99]
    }
]

print(f"The features of the batch 2nd member are : {batch[1]["features"]}")