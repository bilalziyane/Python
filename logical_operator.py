temp=int(input("what's the temperature outside?\n"))
if not(temp>=0 and  temp<=30):
    print("stay home!")
elif not(temp<0 or temp>30):
    print("the temperature is good today !")
    print("think about hanging  out! ")
