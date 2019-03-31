l=int(raw_input("How many ractangle you want to see: "))
l=((l*5)+1)
m=l-1
for i in range (1,6):
    for j in range(1,l):
         if i == 1 or i == 5 or j % 5==0  or j == 1:
             print "*",
             if j % 5==0 and j != m:
                print "*",
                j=j+1
         else:
             print " ",
    print