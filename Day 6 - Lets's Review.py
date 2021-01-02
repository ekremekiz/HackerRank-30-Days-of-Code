# Enter your code here. Read input from STDIN. Print output to STDOUT
s_len = input()
for i in range(int(s_len)):
    string = input()
    char = []
    char[:0] = string
    cift=""
    tek=""
    for j in range(len(char)):
        if j % 2 != 0:
            tek += char[j]
        else:
            cift += char[j]
    print(cift + " " + tek)
