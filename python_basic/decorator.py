import time 

def execution_timer(func):

    def wrapper():
    start=time.time()
    func()
    end=time.time()

    return wrapper
@execution_timer
def train_heavy_model():
    time.sleep(2)
    print ("Model training complete!")

train_heavy_model()

    