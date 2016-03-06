from math import log
from random import random

from src.fixed_length_encoder import fixed_length_encoder
from src.operations_on_msg import *

if __name__ == '__main__':
    Nsymb = 20
    t = [0.01, 0.02, 0.03, 0.04, 0.05, 0.05, 0.3, 0.5]
    print t

    p = [0]
    for count in range (1, len(t)):
        p.append(p[count-1] + t[count - 1])

    print p

    sum = 0
    for i in t:
        avg = i*log(1/i,2)
        sum += avg
    entropy = sum
    print "entropy =", entropy

    r = random()

    x = []
    for i in range (0, Nsymb):
        r = random()
   #     print r
        index = -1
        for k in range(0, len(p)):
            if (r-p[k] > 0):
                if (k > index):
                    index = k

        x.append(index);

    #print x

# codebooks
    codeword_y1 = [ '000', '001', '010', '011', '100', '101', '110', '111' ]

    codeword_y2 = [ '000000', '000001', '00001', '0010', '0011', '0001', '01', '1' ]

    codeword_y3 = [ '0000001', '000010', '000001', '00010', '00110', '00100', '01', '1' ]

    print codeword_y1

    msg1 = fixed_length_encoder(codeword_y1, Nsymb, x)

    msg1_string = msg_toString (msg1, t)

    msg_efficiency(msg1, entropy, t)

    msg_n_1bits(msg1_string)