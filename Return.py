#Import modules : ListSplit and DateTime
import DateTime
import ListSplit
ListSplit.Lsplit()
#Define a function named ReturnBook
def ReturnBook():
    Fname=input("Enter the first name of the borrower: ")
    Bow="Borrower-"+Fname+".txt"
    #Exception handling
    try:
        with open(Bow,"r") as f: #Open Bow and enable reading
            Line=f.readlines() # Read each line of the text 
            Line=[Bow.strip("$") for Bow in Line] #Removes "$" from the lines
            
        with open(Bow,"r") as f: #Open Bow and enable reading
            Info=f.read() #Reads the entire file
            print(Info) #Displays the note in Bow file
    except:
        print("Incorrect Name of the borrower.Please enter the correct name.")
        ReturnBook() #Call the function RetunBook()

    Ret="Return-"+Fname+".txt" #Create a text file
    with open(Ret,"w+") as f: #Opening Ret for writing
        #Note for Return
        f.write("           \t\t\tLibrary Management System           \n")
        f.write("\n\nReturn Date: " + DateTime.Date()+" Time:"+ DateTime.Time())
        f.write( "\n" + "Returned By: "+Fname+"\n\n")
        f.write("S.N.\t\t\tBookName\t\t\t\tCost\n")

    TotalCost=0.0   
    for i in range(5):
        if ListSplit.BookName[i]in Info:
            with open(Ret,"a") as f: #Opens file Ret and enable the append mode
                #Add the note to the file
                f.write(" "+str(i+1)+"\t\t\t"+ ListSplit.BookName[i]+"\t\t\t$"+ListSplit.Cost[i]+"\n")
                ListSplit.Quantity[i]=int(ListSplit.Quantity[i])+1 #Increse the quantity of books after returning
            TotalCost+=float(ListSplit.Cost[i])
            
    print("\t\t\t\t\t\t\t\t\t\t  "+"Total: "+"$"+str(TotalCost))
    #To add fine if the book is returned late
    print("Is the book returned late?")
    print("Press Y for Yes and N for No")
    s=input()
    if s.upper()=="Y": #upper() converts all lowercase letter in a string to uppercase
                       #and returns the modified string
        print("How late was the book returned?")
        NoOfDay=int(input())
        Fine=1.5*NoOfDay #Adds extra charge for late return
        with open(Ret,"a")as f:#Opens file Ret and enable the append mode
            f.write("\t\t\t\t\t\t\t Fine:  $"+ str(Fine)+"\n")
        TotalCost=TotalCost+Fine
        print("Final Total: "+ "$"+str(TotalCost))
    with open(Ret,"a")as f:
        #Add note to the text file 
        f.write("\t\t\t\t\t\t\t Total: $"+ str(TotalCost))
    
        #Opening LibraryStock.txt for writing
    with open("LibraryStock.txt","w+") as f:
            for i in range(5):
                #Write a note to the file
                f.write(ListSplit.BookName[i]+","+ListSplit.AuthorName[i]+","+str(ListSplit.Quantity[i])+","+"$"+ListSplit.Cost[i]+"\n")

                


      
             
            
                    
        
            
