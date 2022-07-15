#Define a function named Date
def Date():
    import datetime
    D=datetime.datetime.now #Current Date and Time
    return str(D().date()) #Returns current Date
   	
#Define a function named Time
def Time():
    import datetime
    T=datetime.datetime.now #Current Date and Time
    return str(T().time())#Returns current Time
    
    


