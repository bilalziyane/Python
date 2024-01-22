#dictionnary A changeable, unordered collection of unique key:value pairs fast becaause they use hashing , allow us to access a value quickly


capitals={'USA':"Washigton Dc",
          "India":"New Delhi",
          "China":"beijing",
          "Russia":"Moscow"}

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"LA"})
capitals.pop("China")
#capitals.clear()

#print(capitals["Russia"])
print(capitals.get("morocco"))#this is a better way to check if an element exists in a dictionnary or not
#print(capitals.values()) 
#print(capitals.keys()) 
#print(capitals.items())

for key,value in capitals.items():
    print(key,value)
