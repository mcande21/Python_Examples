# example of reading a file from python

# step one: open a file for reading (this is the default way a file is opened in python
f = open("words.txt")

# we can use a for loop for every line in file
for line in f:
    # line will still contain the newline character from the end of the line
    # we can remove this (along with any other spaces or tabs that are at
    # the end of the line) with the "rstrip" method
    print(line.rstrip())

# close the file
f.close()