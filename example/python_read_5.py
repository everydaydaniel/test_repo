# from sys module import a member called 'argv'
from sys import argv
#unpack
# test 5 - test PR title
script, filename = argv
fp = open(filename)
print "Reading files accross multiple files %r " % fp
print fp.read()
print("finished")
fp.close()
