import sys

words = sys.stdin.read().split()            #Reads the imported files

x = len(words)                              #Stores the length of all the words
y1 = 0
y2 = 0                                      #Iterable variable
z = 0

for y1 in range(1, x):                          #Loop for each "word" in file
    if y1 % 2:                               #Sum of the numbers provided
        a = words[y1]
        z += int(a)
    y1 += 1

z = (y1-1)/100                              # Converts to percentage, doesn't work without the -1, not sure why

for y2 in range(x):
    if y2 % 2:                               #Based on file output find numbers
        b = (int(words[y2]) / z)
        print("\t", "[", end="")
        for b in range(int(b)):             #Asterix printer
            print("*", end="")
        print("]", end="")
        print("", b, "%")

    else:                                   #Prints words
        c = words[y2]
        print(c, end="")
    y2 += 1