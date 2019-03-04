# from sys module import a member called 'argv'
from sys import argv
#unpack
# test 6 - test PR title yadda
scripts, filenames = argv
fp = open(filenames)
print "Reading file names %r " % fp
print "read some more files %r " % fp
print fp.read()
fp.close()
print("more lines")
print("made a new branch")
print("more lines")
print("actually one more line")
print("more lines")
print("actually one more line")
