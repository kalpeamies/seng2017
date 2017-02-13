#!/usr/bin/python
# -*- coding: utf-8 -*-

lowCipher = u"abcdefghijklmnopqrstuvwxyz"
capCipher = u"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
miscCipher = u"!\"#€%&/()="
numCipher = u"1234567890"

def encode(inputString):
    if not isinstance(inputString,basestring):
        raise TypeError
    if len(inputString) > 1000:
        raise ValueError
    outputString = ""
    for i in inputString:
        if i in lowCipher:
            o = capCipher[(lowCipher.index(i) + 13) % len(lowCipher)]
        elif i in capCipher:
            o = lowCipher[(capCipher.index(i) + 13) % len(capCipher)]
        elif i in miscCipher:
            o = numCipher[miscCipher.index(i)]
        elif i in numCipher:
            o = miscCipher[numCipher.index(i)]
        else:
            raise ValueError
        outputString += o
    return outputString

def decode(inputString):
    return encode(inputString)

# if __name__ == "__main__":
#     print len(lowCipher)
#     print len(capCipher)
#     print len(miscCipher)
#     print len(numCipher)
#     inputString = raw_input("Input:")
#     print encode(inputString)
#     print decode(inputString)
