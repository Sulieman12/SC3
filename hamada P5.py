def bye(filename):
    f = open(filename, 'r')
    char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,:/?! '
    diction = {}
    msg = ''

    for line in f:
        msg += line

    for i in char:
        diction[i] = 0

    for i in msg:
        diction[i] += 1

    print(diction)
    f.close
=========================================================================
from Sulieman import *
bye('BYE.txt')
=================================================
