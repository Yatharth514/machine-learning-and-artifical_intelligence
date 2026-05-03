class RobotPosition:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @classmethod
    def from_gps_string(cls,data_string):
        first,second=data_string.split('-')
        X,x=first.split(':')
        Y,y=second.split(':')
        return cls(int(x),int(y))
    @staticmethod
    def is_within_bounds(x,y):
        return 0<=x<=100 and 0<=y<=100
    
print(RobotPosition.is_within_bounds(105,50))

position=RobotPosition.from_gps_string("X:15-Y:30")
        