# from sys module import a member called 'argv'
from sys import argv
#unpack
# test 5 - test PR title
script, filename = argv
fp = open(filename)
print "And I moddified this line %r " % fp
print fp.read()
print("I added a new line to Johns code")
print("finished more changes to this code")
fp.close()
