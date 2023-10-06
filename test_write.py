f = open("test.txt", 'w')
for i in range(1,7):
    data = f"Numbers {i}\n"
    f.write(data)
f.close()

