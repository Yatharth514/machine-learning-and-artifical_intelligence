import pandas as pd

data={
    "Models": ["GPT","Claude","Gemini"],
    "Accuracy": [85.4,98,95.9]
}
df=pd.DataFrame(data)
print("_____Full Dataframes_____")
print(df)

accuracy=df["Accuracy"]
print(f"The mean accuracy is : {accuracy.mean()}")

df["Is_Excellent"]=[True,True,True]
print("_____Full Dataframes_____")
print(df)

new_data={
    "Patient_ID":[7,8,9,10,11],
    "Age":[19,25,39,45,78],
    "Had_Disease":[False,True,True,False,True]
}
df2=pd.DataFrame(new_data)
print("____First 3 Patient____")
print(df2.head(3))

infected_patient=df2[df2["Had_Disease"]==True]
print("____Patient with disease___")
print(infected_patient)


prev_data = {
    "Age": [25, 30, 22, 35],
    "Income": [50000, 70000, 45000, 90000],
    "Purchased_AI_Course": [True, True, False, True]
}
df3=pd.DataFrame(prev_data)

income=df3["Income"]
print(f"The highest income : {income.max()}")
person_max=df3[df3["Income"]==income.max()]
print(person_max)