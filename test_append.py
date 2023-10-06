f =open("test.txt", 'a')
for i in range(9, 11):
    data =f"Added numbers {i}!\n"
    f.write(data)
f.close()