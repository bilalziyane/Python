#loop controler = change a loops execution from its normal sequence

# break=     used to terminate the loop entirely
# continue=  skips to the next iteration of the loop
# pass=      does nothing, acts as a placeholder

while True:
    name=input("enter your name ")
    if name !="":
        break
phone_number= "123-456-7890"

for i in phone_number:
    if i =="-":
        continue
    print(i,end="")

for j in range(1,21):
    if j ==13:
        pass #continue do the same role
    else :
        print(j)