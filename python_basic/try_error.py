#Theory
data_stream = ["100", "250", "N/A", "400"]
total = 0

for item in data_stream:
    try:
        value = int(item)
    except ValueError:
        print("Bad data encountered. Skipping.")
    else:
        total = total + value
    finally:
        print("Processed an item.")

print(total)

#implementation
incoming_payload = [
    {"user_id": 1, "age": "25"},
    {"user_id": 2, "age": "thirty"},
    {"user_id": 3},
    {"user_id": 4, "age": "42"},
    {"user_id": 5, "age": None}
]
total_age=0
for items in incoming_payload:
    try:
        value=int(items["age"])
    except KeyError:
        print("Does not have an age factor")
    except ValueError:
        print("Bad data encountered,skipping")
    except TypeError:
        print("None value encountered")
    else:
        total_age=total_age+value
    finally:
         print("Processed an item.")

print(total_age)
    