#get input and initialize variables
decimal = int(input("Enter a decimal number \n"))
binary = 0
ctr = 0
temp = decimal  #copy input decimal

#find binary value using while loop
while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1

#output the result       
print("Binary of {x} is: {y}".format(x=decimal,y=binary))
