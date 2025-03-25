# f = open("D://Sowmyashree//happy.txt","w")
# f.write("I love myself")
# f.close()


# f=open("D://Sowmyashree//happ.txt","r")
# print(f.read())
# f.close()

f=open("D://Sowmyashree//happy.txt","r")
for line in f:
    token = line.split('')
print(str(token))
f.close()