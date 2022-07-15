#Defining a function named LSplit
def Lsplit():
    #Declare global variable
    global BookName
    global AuthorName
    global Quantity
    global Cost
    #Initializing the lists
    AuthorName=[]
    BookName=[]    
    Quantity=[]
    Cost=[]

    with open("LibraryStock.txt","r") as file: # Opens the text file named Library.txt
        Line=file.readlines() #Read all the lines at a single go 
        Line=[x.strip('\n') for x in Line] #remove line breaks
        for i in range(len(Line)): 
            index=0  #Initializing index
            for a in Line[i].split(','): #split() will split a string at each seperator
                if(index==0):
                    BookName.append(a)  #append the object to the end of the list.
                    
                elif(index==1):
                    AuthorName.append(a) 
                    
                elif(index==2):
                    Quantity.append(a)
                    
                elif(index==3):
                    Cost.append(a.strip("$"))#remove "$" character 
                #Increment index by one  
                index+=1 
                
