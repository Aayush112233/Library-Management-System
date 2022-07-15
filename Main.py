#Import modules : ListSplit,Borrow,DateTime and Return
import ListSplit
import Borrow
import DateTime
import Return
#Define a function named Main
def Main():
        #Infinite Iteration 
        while(True):
            print("         Welcome To The Library Management System            ")
            print("=============================================================")
            print("Enter 1 : To Display the available books")
            print("Enter 2 : To Borrow a Book")
            print("Enter 3 : To return a Book")
            print("Enter 4 : To Exit ")
            #Exception Handling
            try:
                a=int(input("Select from 1-4 : "))                    
                if(a==1):
                        with open("LibraryStock.txt","r") as f: #Open the txt file named LibraryStock.txt and enable reading
                                line=f.read() #reads the entire file
                                print("The available books are :")
                                print(line)   
                elif(a==2):
                        ListSplit.Lsplit() #Call the function Lsplit() from ListSplit
                        Borrow.BorrowBook() #Call the funtion BorrowBook() from Borrow
                elif(a==3):
                        ListSplit.Lsplit() #Call the function Lsplit from ListSplit
                        Return.ReturnBook() #Call the funtion ReturnBook() from Return
                elif(a==4):
                        print("Thank you for using our Library Management System :)")

                        break #Break the Iteration
                else:
                        print("Please choose from 1 - 4 only.")
            #When an inappropriate value is assigned
            except ValueError:                    
                    print("Invalid Input, Try Again as mentioned")  
Main()              

                    
