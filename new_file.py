weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
with open("file.txt", "w") as file:
    for day in weekdays:
        file.write(day + "\n")

with open("file.txt", "r") as file:
    content = file.read()

    print(content)