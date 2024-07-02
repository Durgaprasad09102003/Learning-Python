#write a python program to implement files and its methods

#installing the files in the program


print("\n")
#methods in files

#open()
f=open('sample.txt','w')
f.write("apple")

#write(strings)
f=open('lang.txt','w')
f.write("python programming")

#writelines()
g=open('subjects.txt', 'w')
g.writelines(['c\n', 'python\n', 'java\n', 'c++\n'])

#read()
g=open('subjects.txt','r')
print(g.read())

#read(n)
g=open('subjects.txt','r')
print(g.read(15))

#readline()
g=open('subjects.txt', 'r')
print(g.readline())

#readlines()
g=open('subjects.txt', 'r')
print(g.readlines())

#close
g=open('subjects.txt', 'r')
print(g.readline())
f.close()

#with statements
with open('subjects.txt','r') as g:
    print(g.read(7))
    
g=open('subjects.txt', 'r')
print(g.readable())
print(g.writable())
print("position of the file is ",g.tell())
print(g.read())
print('after reading position of file object is', g.tell())
print('file description is',g.fileno())

#seek()
g=open('subjects.txt','r')
g.seek(2)
print(g.readline())

#seekable()
g=open('subjects.txt', 'r')
print(g.seekable())

#isatty()
g=open('subjects.txt', 'r')
print(g.isatty())

#truncate()
g=open('subjects.txt', 'a')
g.truncate(5)
g.close()
g=open('subjects.txt','r')
print(g.read())

#flush()
g=open('subjects.txt', 'r')
print('name of the file ',g.name)
g.flush()
g.close()
    