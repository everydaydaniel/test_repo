# from sys module import a member called 'argv'
from sys import argv
#unpack
# test3
script, filename = argv
fp = open(filename)
print "Reading files %r " % fp
print fp.read()
fp.open()
from sys import argv
#unpack
# test3
script, filename = argv
fp = open(filename)
print("something new")
print "Reading file %r " % fp
print fp.read()
fp.close()
