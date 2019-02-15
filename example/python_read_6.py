# from sys module import a member called 'argv'
from sys import argv
#unpack
# test 6 - test PR title yadda
script, filename = argv
fp = open(filename)
print "Reading file names %r " % fp
print "read some more files %r " % fp
print fp.read()
fp.close()
print("more lines")
print("actually one more line")
print("more lines")
print("actually one more line")
print("more lines")
print("actually one more line")
