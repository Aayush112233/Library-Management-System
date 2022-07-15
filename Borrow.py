#Import modules : ListSplit and DateTime
import ListSplit
import DateTime
#Define a function named BorrowBook
def BorrowBook():
    Borrow = False
    while(True): 
        FirstName = input("What is your first name? ")      
 
        # Check the value is a alphabet
        if FirstName.isalpha() == True:
            break #Terminates the loop      
        else:
            print("Type your name from A-Z only")
        
    while(True):
        LastName = input("What is your last name? ")

        # Check the value is a alphabet
        if LastName.isalpha() == True:
            break #Terminates the loop          
        else:
            print("Type your name from A-Z only")
            
    Bow="Borrower-"+FirstName+".txt" #Creating a text file
    with open(Bow,"w+") as f:  #Opening Bow for writing
        # Note for Borrow
        f.write("           \t\t\tLibrary Management System           \n")
        f.write("\n\nBorrowed Date: " + DateTime.Date()+" Time:"+ DateTime.Time())
        f.write( "\n" + "Borrowed By: "+FirstName+" "+LastName+"\n\n")
        f.write("S.N.\t\t BookName\t\t\t   AuthorName\t\t\tCost")

    count = 1 
    while Borrow==False:
        print("Select a option from below:") 
        for i in range(len(ListSplit.BookName)): 
            print("Enter", i, "to borrow book", ListSplit.BookName[i])
    #Exception Handling
        try:   
            a=int(input())
            try:
                if(int(ListSplit.Quantity[a])>0): #Checks if the book is in stock
                    print("Book is available to borrow")
                    with open(Bow,"a") as f: #Opens file Bow and enable the append mode
                        #Add a note to the text file 
                        f.write("\n "+str(count)+".\t\t"+ ListSplit.BookName[a]+"\t"+ListSplit.AuthorName[a]+"\t\t\t$"+" "+ListSplit.Cost[a]+"\n")
                    ListSplit.Quantity[a]=int(ListSplit.Quantity[a])-1 #Decreasing the value of book quantity after borrow
                    with open("LibraryStock.txt","w+") as f:#Opening LibraryStock.txt for writing
                        for i in range(5):
                             f.write(ListSplit.BookName[i]+","+ListSplit.AuthorName[i]+","+str(ListSplit.Quantity[i])+","+"$"+ListSplit.Cost[i]+"\n")

                    #TO borrow more books.
                    L=True                           
                    while (L==True):
                        More = input("Do you want to borrow more books?(Y/N): ")
                        if More.upper()=="Y":
                            count = count+1
                            print("Select a book from below: ")
                            for i in range(len(ListSplit.BookName)):
                                print("Enter", i, "to borrow book", ListSplit.BookName[i])                            
                            a=int(input())
                            if (int(ListSplit.Quantity[a])>0): #Checks if the book is in stock
                                print("Book is available")
                                with open(Bow,"a") as f:
                                    #Add the note to the file 
                                    f.write(" "+str(count)+". \t\t"+ ListSplit.BookName[a]+"\t\t"+ListSplit.AuthorName[a]+"\t\t$"+" "+ListSplit.Cost[a]+"\n")
                                ListSplit.Quantity[a]=int(ListSplit.Quantity[a])-1 #Decreasing the quantity of book after borrowing
                                with open("LibraryStock.txt","w+") as f:#Opening LibraryStock.txt for writing
                                    for i in range(5):
                                        f.write(ListSplit.BookName[i]+","+ListSplit.AuthorName[i]+","+str(ListSplit.Quantity[i])+","+"$"+ListSplit.Cost[i]+"\n")
                                        Borrow=False
                            else:
                                L=False
                                break #Termminates the Loop
                        elif More.upper()=="N":
                            print("The book have been borrowed sucessfully. Thank You!\n")
                            L=False
                            Borrow = True
                        else:
                            print("Please select as mentioned.")                                        
                else:
                    print("This book is not available to borrow.")
                    BorrowBook() #Call the borrow function
                    Borrow=False 
            #If code is trying to access an index that is invalid.
            except IndexError:
                print("Incorrect choice.Please choose the number correctly.\n")
            #When an inappropriate value is assigned
        except ValueError:
            print("Choose as shown in the Options.\n")
               
                        
    

        
        
        
            
            



