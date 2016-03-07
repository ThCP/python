from math import log
from random import random

from src.encoders import *
from src.operations_on_msg import *
from src.decoders import *
if __name__ == '__main__':
    Nsymb = 20
    t = [0.01, 0.02, 0.03, 0.04, 0.05, 0.05, 0.3, 0.5]
    print t

    p = [0]
    for count in range(1, len(t)):
        p.append(p[count-1] + t[count - 1])

    print p

    sum = 0
    for i in t:
        avg = i*log(1/i, 2)
        sum += avg
    entropy = sum
    print "entropy =", entropy

    r = random()

    x = []

    for i in range(0, Nsymb):
        r = random()
        index = -1
        for k in range(0, len(p)):
            if (r-p[k] > 0):
                if (k > index):
                    index = k

        x.append(index)

    # codebooks
    y1 = ['000', '001', '010', '011', '100', '101', '110', '111']

    y2 = ['000000', '000001', '00001', '0010', '0011', '0001', '01', '1']

    y3 = ['0000001', '000010', '000001', '00010', '00110', '00100', '01', '1']

    print "############# Fixed length encoder #############"

    msg1 = fixed_length_encoder(y1, Nsymb, x)

    msg1_string = msg_toString(msg1, t)

    msg_efficiency(msg1, entropy, t)

    msg_n_1bits(msg1_string)

    print "############# Huffman encoder #############"

    msg2 = huffman_encoder(y2, Nsymb, x)

    msg2_string = msg_toString (msg2, t)

    msg_efficiency(y2, entropy, t)

    msg_n_1bits(msg2_string)

    print "############# Generic encoder #############"

    msg3 = generic_encoder(y3, Nsymb, x)

    msg3_string = msg_toString (msg3, t)

    msg_efficiency(y3, entropy, t)

    msg_n_1bits(msg3_string)

###########################   DECODING

    print "############# Fixed length encoder #############"
    decoded_msg = decoder_fixed_length(msg1_string, y1)

    print "original message = ",x
    print "decoded message =  ",decoded_msg

    print "#############   Huffman encoder    #############"
    decoded_msg = decoder_variable_length(msg2_string, y2)

    print "original message = ",x
    print "decoded message =  ",decoded_msg

    print "#############   Generic encoder    #############"
    decoded_msg = decoder_variable_length(msg3_string, y3)

    print "original message = ",x
    print "decoded message =  ",decoded_msg



