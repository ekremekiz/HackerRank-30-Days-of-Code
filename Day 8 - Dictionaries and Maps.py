# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
phoneBook = {}

for i in range(int(n)):
    newPerson = input()
    name, phone = newPerson.split(" ")
    phoneBook[name] = phone

while 1:
    try:
        query = input()
        if query in phoneBook:
            print(query + "=" + phoneBook[query])
        else:
            print("Not found")
    except:
        break
            
