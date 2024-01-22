#list=used to store multiple items in a single variable

food=["pizza","hamburger","hotdog","spaghetti"]
food[0]="sushi"
print(food[0])
food.append("ice cream")#adds an element at the end of the list
food.remove("hotdog")#removes an element of a list
food.pop()#removes the lats element in the list
food.insert(0,"cake")#insert an element ina definite position
food.sort()#sort  a list alphatecly
food.clear()
for x in food:
    print(x)