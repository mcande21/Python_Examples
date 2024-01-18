# example of wrtiting text/data to a file using python

# first step: open a file for writing
# This clears out the contents of any existing file.

f = open("example_output.txt", "w")

# next step: use python to write text to the file
# write does not automatically produce a new line in the file
f.write("Hello world!\n")
f.write("I like to eat chicken fingers with mayo and ketchup.")

# final step: Close the file
f.close()