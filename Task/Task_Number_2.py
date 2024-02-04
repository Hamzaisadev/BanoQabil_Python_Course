#name: hamza
#emil: ishaqhamza212@gmail.com
#rollnumber: 33090

#choice simple calculator mayde by Hamza/me,Also my first programme
#i know i made this code terribly long but as i said this is my first programme
#first lets give welcome statement with print
print("Welcome To My Calculator")
print("=========================")
#lets ask user to choose opreation
print("Choose opreation")
print("=========================")
print("1.Adition")
print("2.Diffrence")
print("3.Division")
print("4.Multiplication") 
print("===============") 
#now i will use while loop so user can perfom calcultions as much as he wants
while True:
    #everthing i did here is under while block
    #here i will take input from user what he wants to do 
    
    choice =int(input("Select 1/2/3/4 :"))
    
    #here i used condition if to show error i stated that if value of variable "choice" is > 4 print(error)
    
    if choice >4:
     print ("ERROR!!!Please choose from the given options")
     #here i used 'continue' to start again if error came
     continue
 #of course here i took input from user to 
    first_num=int(input("Enter first number:"))
    second_name=int(input("Enter Second number:"))
    #i am using if condition for calcultions with == opretor
    if  choice==1:
        total= first_num + second_name
        print(total)
    if  choice==2:
     total= first_num - second_name
     print(total)
    if  choice==3:
     total= first_num / second_name
     print(total)
    if  choice==4:
     total= first_num * second_name
     print(total)

    print ("========================================")
    #lets ask user if he even wants to continue or not
    again =  input("Do you Wish To Continue (y/n) :")
    #again using if conditions
    
    if again == "n":
         print ("Hogaya lakhon ka hisaab")
         print ("Thanks for using my calculator")
         break

    

#ok this was hard to do without def and this is also my first program

    
