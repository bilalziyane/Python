import time
#name="" 
#while len(name)==0:
#    name =input("what's your name ? ")
#print("hello Mr."+name.capitalize()) 
#lastname=None
#while not lastname:
#    lastname=input(("what's your last name?"))
#print("greeting Mr."+lastname.capitalize())



#for i in range(10):
#    print(i+1)

#for i in range(50,100+1,2):
#    print(i)

#for i in "bilal ziyane":
#    print (i)

#for seconds in range(10,0,-1):
#    print(seconds )
#    time.sleep(1)
#print("happy new year!")



rows=int(input("how many rows do you want? "))
columns=int(input("how many columns do you want? "))
symbol = input("enter a symbol to use: ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end="")
    print() #you must be careful with emplacement in for loop
   