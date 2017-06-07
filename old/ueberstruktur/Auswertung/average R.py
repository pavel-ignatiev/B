import fileinput
from sys import argv
import numpy as np
import matplotlib.pyplot as plt


f = open(argv[1])
s = open('argv[2]','wb')
tabelle = f.read()
tabelle = tabelle.split()
print tabelle
s.write(tabelle)
s.close()
f.close()
#print "%s" %tabelle
for line in tabelle:
        print(repr(line))






