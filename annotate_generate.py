file=open("info.txt","w")
for i in range (1424):
        if i<700:
                file.write(str(i)+".png , 0 \n ")
        else:
                file.write(str(i)+".png , 1 \n ")
file.close()


