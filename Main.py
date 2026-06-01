import os
with open("hello.txt","w" ) as f:
    f.write("Hello there.")
with open("cba.txt","r") as Fnumber2:
    stuff = Fnumber2.readlines()
    for line in stuff:
        word = line.split()
        print(word)
if os.path.exists("hello.txt"):
    os.remove("hello.txt")
else:
    with open("hello.txt","x") as f:
        pass