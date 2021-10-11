print("Enter the Decimal Number: ")
dnum = int(input())
i = 0
bnum = []
while dnum!=0:
    rem = dnum%2
    bnum.insert(i, rem)
    i = i+1
    dnum = int(dnum/2)

i = i-1
print("\nEquivalent Binary Value is:")
while i>=0:
    print(end=str(bnum[i]))
    i = i-1
print()
