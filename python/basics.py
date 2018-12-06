
############ Pickle
"""
Pickling:

Literally, the term pickle means storing something in a saline solution. 
Only here, instead of vegetables its objects. Not everything in life can 
be seen as 0s and 1s (gosh! philosophy), but pickling helps us achieve that
since it converts any kind of complex data to 0s and 1s (byte streams). 
This process can be referred to as pickling, serialization, flattening or 
marshalling. The resulting byte stream can also be converted back into Python 
objects by a process known as Unpickling.

The real world uses of Pickling and Unpickling are widespread as they allow you
to easily send data from one server to another, and store it in a file or database.

Advantages
Helps in saving complicated data.
Quite easy to use, doesn’t require several lines of code and hence not bulky.
Saved data is not so readable hence provides some data security.

"""

#pickle
import pickle
emp = {1:"A",2:"B",3:"C",4:"D",5:"E"}
pickling_on = open("Emp.pickle","wb")
pickle.dump(emp, pickling_on)
pickling_on.close()

#unpickle
pickle_off = open("Emp.pickle","rb")
emp = pickle.load(pickle_off)
print(emp)



###############
#open files and modes

#To open a text file, use:
fh = open("hello.txt", "r")

#To read a text file, use:
fh = open("hello.txt","r")
print fh.read()

#To read one line at a time, use:
fh = open("hello".txt", "r")
print fh.readline()

#To read a list of lines use:
fh = open("hello.txt.", "r")
print fh.readlines()

#To write to a file, use:
fh = open("hello.txt","w")
write("Hello World")
fh.close()

#to write to a file, use:
fh = open("hello.txt", "w")
lines_of_text = ["a line of text", "another line of text", "a third line"]
fh.writelines(lines_of_text)
fh.close()

#To append to file, use:
fh = open("Hello.txt", "a")
write("Hello World again")
fh.close()

#To close a file, use
fh = open("hello.txt", "r")
print fh.read()
fh.close()

# On Windows, 'b' appended to the mode opens the file in binary mode, so there are also modes like 'rb', 'wb', and 'r+b'.

open("hello.txt","rb")

############
