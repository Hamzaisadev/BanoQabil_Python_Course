#Name: Hamza
#rollnum: 33090
#email: Ishaqhamza212@gmail.com
print("Welcome To Unit Converter")
print("===========================")
print("Mode Selection Menu")
print("===========================")

print("1. length")
print("2. Mass")
print("3. Temperature")
print("4. Time")
print("5. Exit")
print("===========================")

while True:
  mode = int(input("Enter your mode from 1 to 4 : "))
  print("===========================")

        # ... (rest of your length mode code goes here, properly indented
#======= length ========
#===== using conditiion for Calculations======
  if mode == 5:
    print("Thank you for using Unit Converter")
    break

  if mode >= 6:
    print("Invalid input")
    continue

    
  if mode ==1:
    while True:
      print("=======================")
      print("you are in length mode")
      print("=======================")
      print("Select conversion unit")
      print("1. Centimeter to Kilometer") 
      print("2. Centimeter to Meter") 
      print("3. Centimeter to Inch")
      print("4. Centimeter to Mile")
      print("5. Kilometer to Centimeter")
      print("6. Kilometer to Meter")
      print("7. Kilometer to Inch")
      print("8. Kilometer to Mile")
      print("9. Meter to Centimeter")
      print("10. Meter to Inch")
      print("11. Meter to Kilometer")
      print("12. Meter to Mile")
      print("13. Inch to Centimeter")
      print("14. Inch to Meter")
      print("15. Inch to Centimeter")
      print("16. Inch to Mile")
      print("17. Mile to Centimeter")
      print("18. Mile to Meter")
      print("19. Mile to Kilometer")
      print("20. Mile to Inch")
      print("21. Exit here")
  
  #=== using conditiion for Calculations======
  
  #created a variable to know what user wants to do 

   
      length= int(input("Select conversion from 1 to 21 : "))
    
    # Adding a break statement to exit the while loop when user wants
    
      if length == 21:
        print("you selected to exit length mode")
        break

      #making an error with if condition 
      if length >= 22:
        print("INVALID INPUT PLEASE SELECT FROM 1 TO 21")
        continue

      #calculations for length mode
      
   #1.  centimeter to kilometer
   #Formula	divide the length value by 100000
      
      if length == 1 :
        print("you selected to convert Centimeter to Kilometer")
        centimeter = int(input("Enter Centimeter here : ")) 
        kilometer = centimeter / 100000 #
        print(kilometer)
       
#2. centimeter to meter
#Formula divide the Length by 100
       
      if length == 2 :
       print("you selected to convert Centimeter to Meter")
       centimeter = int(input("Enter Centimeter here : "))
       meter = centimeter / 100
       print(meter)
     
#3. centimeter to inch
#Formula	divide the length value by 2.54
     
      if length == 3 :
       print("you selected to convert centimeter to inch")
       centimeter = int(input("Enter centimeter here : "))
       inch = centimeter / 2.54
       print(inch)
      
    #4. centimeter to mile
    #Formula	for an approximate result, divide the length value by 160900
      
      if length == 4 :
        print("you selected to convert Centimeter to Mile")
        centimeter = int(input("Enter Centimeter here : "))
        mile = centimeter / 160900
        print(mile)
      
  #kilometer to centimeter
  #Formula	multiply the length value by 100000
  
      if length == 5 :
        print("you selected to convert Kilometer to Centimeter")
        kilometer = int(input("Enter Kilometer here : "))
        centimeter = kilometer * 100000
        print(centimeter)
  
  #kilometer to meter
  # Formula	multiply the length value by 1000
  
      if length == 6 :
        print("you selected to convert Kilometer to Meter")
        kilometer = int(input("Enter Kilometer here : "))
        meter = kilometer * 1000
        print(meter)
      
  #kilometer to Inch
  #Formula	for an approximate result, multiply the length value by 39370
  
      if length == 7 :
        print("you selected to convert Kilometer to Inch")
        kilometer = int(input("Enter Kilometer here : "))
        inch = kilometer * 39370
        print(inch)
    
    #kilometer to Mile
    #Formula	for an approximate result, divide the length value by 1.609
    
      if length == 8 :
        print("you selected to convert Kilometer to Mile")
        kilometer = int(input("Enter kilometer here : "))
        mile = kilometer /1.609
        print(mile)
        
    #meter to centimeter
    #Formula	multiply the length value by 100 
    
      if length == 9 :
        print("you selected to convert Meter to Centimeter")
        meter = int(input("Enter Meter here : "))
        centimeter = meter * 100
        print(centimeter)
    
    #meter to Inch
    #Formula	multiply the length value by 39.37
    
      if length == 10 :
        print("you selected to convert Meter to Inch")
        meter = int(input("Enter Meter here : "))
        inch = meter * 39.37
        print(inch)
        
    #meter to kilometer
    #Formula	divide the length value by 1000
    
      if length == 11 :
        print("you selected to convert Meter to kilometer")
        meter = int(input("Enter Meter here : "))
        kilometer = meter / 1000
        print(kilometer)
        
    #meter to Mile
    #Formula	for an approximate result, divide the length value by 1609
    
      if length == 12 :
        print("you selected to convert Meter to Mile")
        meter = int(input("Enter Meter here : "))
        mile = meter / 1609
        print(mile)
        
    #Inch to centimeter
    #Formula	multiply the length value by 2.54
    
      if length == 13 :
        print("you selected to convert Inch to Centimeter")
        inch = int(input("Enter Inch here : "))
        centimeter = inch * 2.54
        print(centimeter)
        
    #Inch to meter
    #Formula	divide the length value by 39.37
    
      if length == 14 :
        print("you selected to convert Inch to Meter")
        inch = int(input("Enter Inch here : "))
        meter = inch / 39.37
        print(meter)
    
    #Inch to kilometer
    #Formula	for an approximate result, divide the length value by 39370
    
      if length == 15 :
        print("you selected to convert Inch to kilometer")
        inch = int(input("Enter Inch here : "))
        kilometer = inch / 39370
        print(kilometer)
        
    
    #Inch to Mile
    #Formula	divide the length value by 63360
    
      if length == 16 :
        print("you selected to convert Inch to Mile")
        Inch = int(input("Enter Inch here : "))
        mile = inch / 63360
        print(mile)
        
    #Mile to centimeter
    #Formula	for an approximate result, multiply the length value by 160900
    
    
      if length == 17 :
        print("you selected to convert Mile to Centimeter")
        mile = int(input("Enter Mile here : "))
        centimeter = mile *160900
        print(centimeter)
        
    #Mile to meter
    #Formula	for an approximate result, multiply the length value by 1609
    
      if length == 18 :
        print("you selected to convert Mile to Meter")
        mile = int(input("Enter Mile here : "))
        meter = mile * 1609
        print(meter)
    
    #Mile to kilometer
    #Formula	for an approximate result, multiply the length value by 1.609
    
      if length == 19 :
        print("you selected to convert Mile to Kilometer")
        mile = int(input("Enter Mile here : "))
        Kilometer = mile * 1.609
        print(Kilometer)
    
    #Mile to Inch
    #Formula	multiply the length value by 63360
      
      if length == 20 :
        print("you selected to convert Mile to Inch")
        mile = int(input("Enter Mile here : "))
        inch = mile * 63360
        print(inch)


#here i am done with length    

# Add similar if-else blocks for other modes (temperature, mass, time)
 
  if mode == 2:
    while True:
      print("=======================")
      print("you are in Mass mode")
      print("=======================")
      print("Select conversion unit")
      print("1. Kilogram to Pound")
      print("2. Kilogram to Tonne")
      print("3. Pound to Kilogram")
      print("4. Pound to Tonne")
      print("5. Tonne to Kilogram")
      print("6. Tonne to Pound")
      print("7. Exit here")
      print("=======================")
      # ... (rest of your mass mode code goes here, properly indented
#======= Mass ========
#===== using conditiion for Calculations======
      mass = int(input("Select conversion from 1 to 7 : "))
      #add a break statement to exit the while loop when user wants

      if mass == 7:
        print ("you selected to exit Mass mode")
        break

#making an error with if condition
      if mass >=8:
        print("INVALID INPUT PLEASE SELECT FROM 1 TO 7")
        continue
        
               

      #kilogram to pound
#formulat	multiply the mass value by 2.205


      if mass == 1:
        print("you selected to convert Kilogram to Pound")
        kilogram =int("Enter Kilogram here :")
        pound = kilogram *2.205
        print(pound)

#kilogram to tonne
#Formula	divide the mass value by 1000

      if mass == 2:
        print("You selected to convert Kilogram to Tonne")
        kilogram = int(input("Enter Kilogram here : "))
        tonne = kilogram / 1000
        print(tonne)

#pound to kilogram
#Formula	divide the mass value by 2.205
      if mass == 3:
        print("You selected to convert Pound to Kilogram")
        pound = int(input("Enter pound here : "))
        kilogram = pound / 2.205
        print("kilogram") 

#pound to tonne
#Formula	divide the mass value by 2205

      if mass == 4:
        print("You have selected to convert pound to tonne")
        pound = int(input("Enter pound here : "))
        tonne = pound / 2205
        print(tonne)
        
#tonne to kilogram
#Formula	multiply the mass value by 1000

      if mass == 5 :
        print ("You have select to convert tonne to kilogram")
        tonne = int(input("Enter tonne here : "))
        kilogram = tonne * 1000
        print(kilogram)


#tonne to pound
#Formula	multiply the mass value by 2205

      if mass == 6 :
        print ("You have selected to Convert tonne to pound ")
        tonne = int(input("Enter tonne here : "))
        pound = tonne * 2205
        print(pound)

# mass mode is done

# Add similar if-else blocks for other modes (temperature, time)

#======= Temperature ========
#===== using conditiion for Calculations======


  if mode == 3:
    while True:
      print("=======================")
      print("you are in Temperature mode")
      print("=======================")
      print("Select conversion unit")
      print("1. Celsius to Fahrenheit")
      print("2. Fahrenheit to Celsius")
      print("3. Exit here")
      print("=======================")


# ... (rest of your temperature mode code goes here, properly indented

      temperature = int(input("Select conversion from 1 to 3 : "))
  
  
      #add a break statement to exit the while loop when user wants
  
      if temperature == 3:
        print("you selected to exit Temperature mode")
        break
  
  #making an error with if condition
  
      if temperature >= 4:
        print("INVALID INPUT PLEASE SELECT FROM 1 TO 3")
        continue
  
  #celsius to fahrenheit
  #formula (n°C × 9/5) + 32 = n°F
  
      if temperature == 1:
        print("you selected to convert Celsius to Fahrenheit")
        celsius = int(input("Enter Celsius here : "))
        fahrenheit = (celsius * 9/5) + 32
        print(fahrenheit)
  
  #fahrenheit to celsius
  #formula (n2°F − 32) × 5/9 = n°C
  
      if temperature == 2:
        print("you selected to convert Fahrenheit to Celsius")
        fahrenheit = float(input("Enter Fahrenheit here : "))
        celsius = (fahrenheit - 32) * 5/9
        print(celsius)
  
  #Temperature is  done
  
  
  # ========Time Converter=======
  #===== using conditiion for Calculations=====

  if mode == 4:
    while True:
      print("=======================")
      print("you are in Time mode")
      print("=======================")
      print("Select conversion unit")
      print("1. Seconds to Minutes")
      print("2. Seconds to Hours")
      print("3. Seconds to Day")
      print("4. minutes to Seconds")
      print("5. minutes to Hours")
      print("6. minutes to Day")
      print("7. Hours to Seconds")
      print("8. Hours to Minutes")
      print("9. Hours to Day")
      print("10. Exit here")
      print("=======================")


# ... (rest of your time mode code goes here, properly indented
      time = int(input("Select conversion from 1 to 10 : "))

#add a break statement to exit the while loop when user wants

      if time == 10:
        print("you selected to exit Time mode")
        break

#making an error with if condition
      if time >= 11:
        print("INVALID INPUT PLEASE SELECT FROM 1 TO 10")
        continue

#seconds to minutes
#formula	divide the time value by 60

      if time == 1:
        print("you selected to convert Seconds to Minutes")
        seconds = int(input("Enter Seconds here : "))
        minutes = seconds / 60
        print(minutes)
      

#seconds to hours
#formula	divide the time value by 3600

      if time == 2:
        print("you selected to convert Seconds to Hours")
        seconds = int(input("Enter Seconds here : "))
        hours = seconds / 3600
        print(hours)

#seconds to day
#formula	divide the time value by 86400
      if time == 3:
        print("you selected to convert Seconds to Day")
        seconds = int(input("Enter Seconds here : "))
        day = seconds / 86400

#minutes to seconds
#formula	multiply the time value by 60

      if time == 4:
        print("you selected to convert Minutes to Seconds")
        minutes = int(input("Enter Minutes here: "))
        seconds = minutes * 60
        print(seconds)
        

#minutes to hours
#formula	divide the time value by 60

      if time == 5:
        print("you selected to convert Minutes to Hours")
        minutes = int(input("Enter Minutes here: "))
        hours = minutes / 60
        print(hours)

#minutes to day
#formula	divide the time value by 1440

      if time == 6:
        print("you selected to convert Minutes to Day")
        minutes = int(input("Enter Minutes here: "))
        day = minutes / 1440
        print(day)

#hours to seconds
#formula	multiply the time value by 3600

      if time == 7:
        print("you selected to convert Hours to Seconds")
        hours = int(input("Enter Hour here : "))

#hours to minutes
#formula	multiply the time value by 60
      if time == 8:
        print("You selected to convert Hours to Minutes ")
        hours = int(input("Enter Hour here : "))
        minutes = hours * 60
        print(minutes)

#hours to day
#formula	divide the time value by 24

      if time == 9:
        print("You selected to convert Hours To Days")
        hours = int(input("Enter Hours here : "))
        days = hours / 24
        print(days)


#time mode is done

#closing the program


      
          


      
      



      
          

          
          
          
      


