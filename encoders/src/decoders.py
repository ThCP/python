def decoder_fixed_length(msg, codeword):
    decoded = []

    max = 0

    for i in range(1, len(codeword)):
        if len(codeword[i]) > len(codeword[max]):
            max = i

    max = len(codeword[max])

    for i in range(0, len(msg), max):
        test = msg[i:i + 3]
        for j in codeword:
            if j == test:
                decoded.append(codeword.index(j))
                break

    return decoded


def decoder_variable_length(msg, codeword):
    decoded = []
    l = 1
    f = 0
    # print codeword
    max = 0

    for i in range(1, len(codeword)):
        if len(codeword[i]) > len(codeword[max]):
            max = i

    max = len(codeword[max])

    i=0
    while i < len(msg):
        for t2 in range(0, max+1):
            test = msg[i:i + t2]
            for k in codeword:
                if test == k:
                    decoded.append(codeword.index(k))
                    f=1
                    l = len(test)
                    # print l
                    break
            if f:
                break
        f = 0
        i+=l
        # print i

    return decoded
