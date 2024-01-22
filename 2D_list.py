#2D list= a listof lists
drinks=["coffee","soda","tea"]
dinner=["pizza","hamburger","hotdog"]
dessert=["cake","ice cream"]

food=[drinks,dinner,dessert]

#print(food[1][1])
for x in food:
    for y in x:
        print(y)