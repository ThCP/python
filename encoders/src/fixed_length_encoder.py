def fle (values, n_bits):
    value = []
    codebook = []
    power = 1
    c = 0
    for i in values:
        codeword = ''

        for j in range(n_bits, 0, -1):
            n = pow(2, j)

            if values.index(i) / j == 0:
                codeword = codeword+"0"
            else:
                codeword = codeword+"1"
        print codeword
        codebook.append(codeword)

if __name__ == '__main__':
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    fle (values, 3)
