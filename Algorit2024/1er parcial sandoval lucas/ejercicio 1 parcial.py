vector=[1,2,3,4,5,6,7,8,9,10]

def invert (vector):
    if len(vector)==1:
        print(vector [0])
    else:
        print(vector[-1])
        invert(vector[:-1])
    
print (invert(vector))